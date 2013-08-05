import sys, os

if len(sys.argv) != 5:
    print "usage: edmpickevents_bsub.py <list_of_events> <Primary Data Set> <njobs> <output_dir>"
    exit(1)

list_of_events = sys.argv[1]
events = open(list_of_events,"r")
event_lines = events.readlines()

dataset = sys.argv[2]
njobs = sys.argv[3]
output_dir = sys.argv[4]
pwd = os.getcwd()

commands = []

#we will pick events once for each event 
for ii in range(len(event_lines)):
    mkdir = "mkdir event_%i; cd event_%i;" % (ii,ii)
    #edmpickevents drops a file named pickevents.root into the directory its called from
    cmd = "edmPickEvents.py --runInteractive \"%s\" %s" % (dataset, event_lines[ii])
    #lets go drop the folder into the output directory
    mvback = "cd ..;mv event_%i %s/res/" % (ii,output_dir)
    commands.append([mkdir,cmd,mvback])                                                       

#write the bsub commands
job = 0
file_counter = 0
cmds_per_job = int(len(commands)) / int(njobs) #integer division
bsub_cmds = []
bsub_file = None

os.system("mkdir " + output_dir)
os.system("mkdir " + output_dir+"/logs")
os.system("mkdir " + output_dir+"/src")
os.system("mkdir " + output_dir+"/res")

#loop over all commands
for ii in range(len(commands)):
	#make sure the extra jobs are added to the last file
	if (file_counter == 0) and (job != njobs):		
		#write a new job
		bsub_file_name = output_dir+"/src/bsub_%i.src" % job
		bsub_file = open(bsub_file_name,"a")
		bsub_file.write('#!/bin/bash\n')
		bsub_file.write("cd %s\n" % pwd)
		bsub_file.write("export SCRAM_ARCH=slc5_amd64_gcc462 \n")
		bsub_file.write("eval `scramv1 ru -sh`\n")

		cmd="bsub -q 1nd "
		cmd+= "-o %s/logs/job_%i.log " % (output_dir ,job)
		cmd+="source "+ bsub_file_name

		bsub_cmds.append(cmd)

		#increment the counter
		job+=1

	bsub_file.write(commands[ii][0])
        bsub_file.write(commands[ii][1])
        bsub_file.write(commands[ii][2])
	
	#if we are at the number of commands per job reset the counter
	if file_counter == cmds_per_job:file_counter = 0		
	elif job == njobs:
		continue
	else:
		file_counter+=1

#print out the submission commands
for ii in bsub_cmds:print ii
