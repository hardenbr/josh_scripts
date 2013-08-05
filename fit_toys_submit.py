import sys, os, random, time

if len(sys.argv) != 6:
    print "usage fit_toys_submit.py <ntoys> <njobs> <input_file_Had> <output_dir> <force_remove=1>"
    exit(1)

ntoys = int(sys.argv[1])
njobs = int(sys.argv[2])
input_file = sys.argv[3]
output_dir = sys.argv[4]+"/"
force_remove = int(sys.argv[5])

if(force_remove): os.system("rm -r " + output_dir)
else: os.system("rm -ri " + output_dir)
#build the directories
os.system("mkdir " + output_dir)
os.system("mkdir " + output_dir+"/logs")
os.system("mkdir " + output_dir+"/src")
os.system("mkdir " + output_dir+"/res")

commands = []

random.seed(time.time())

for ii in range(njobs):
    seed = int(random.random()*1000000)
    
    toy_folder = output_dir+"res/toys_"+str(ii)+"/"
    os.system("mkdir " + toy_folder)
    cmd ="python scripts/runAnalysis.py -a SingleBoxFit -c config_summer2013/SingleBoxFit_Diphoton.cfg --gamma %s  -o %s  --save-toys-from-fit %s  --fitmode 2D -t 200 -i razor_output.root -s %i\n" % (input_file, toy_folder+"toy_output.root", toy_folder, seed)

    commands.append(cmd)

#write the bsub commands
job = 0
file_counter = 0
cmds_per_job = int(len(commands)) / int(njobs) #integer division
bsub_cmds = []
bsub_file = None

for ii in range(len(commands)):
	#make sure the extra jobs are added to the last file
	if (file_counter == 0) and (job != njobs):		
		#write a new job
		bsub_file_name = output_dir+"/src/bsub_%i.src" % job
		bsub_file = open(bsub_file_name,"a")
		bsub_file.write('#!/bin/bash\n')
		bsub_file.write("cd /afs/cern.ch/user/h/hardenbr/2013/RAZOR_DIPHOTON/VECBOS/CMSSW_6_1_1/src/RazorCombinedFit/\n")
		bsub_file.write("export SCRAM_ARCH=slc5_amd64_gcc462 \n")
		bsub_file.write("eval `scramv1 ru -sh`\n")
                bsub_file.write("source setup.sh\n")
                
		cmd="bsub -q 1nd "
		cmd+= "-o %s/logs/job_%i.log " % (output_dir ,job)
		cmd+="source "+ bsub_file_name

		bsub_cmds.append(cmd)

		#increment the counter
		job+=1
                

	bsub_file.write(commands[ii])

        if job != njobs: file_counter+=1        

	#if we are at the number of commands per job reset the counter
	if file_counter == cmds_per_job:file_counter = 0		

#print out the submission commands
for ii in bsub_cmds:print ii
	
