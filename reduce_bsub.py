
import sys, os

if len(sys.argv) != 5:
    print "usage reduce_bsub.py <inputlist> <config> <output_dir> <njobs>"
    exit(1)

pwd = os.getenv("PWD")
input_list = sys.argv[1]
config = sys.argv[2]
output_dir = sys.argv[3]
njobs = int(sys.argv[4])

input = open(input_list,"r")
input_lines = input.readlines()

#remove old instances of the output directory
os.system("rm -r " + output_dir)
#build the directories
os.system("mkdir " + output_dir)
os.system("mkdir " + output_dir+"/logs")
os.system("mkdir " + output_dir+"/src")
os.system("mkdir " + output_dir+"/res")

#build the commands
commands = []
for ii in input_lines:
    name = os.path.basename(ii).rstrip("\n")
    dir = output_dir+"/res"
    outputfile = os.path.join(dir, "red_"+name)
    input_file = ii.rstrip("\n")
    input_list = input_file+".list"

    makelist = "echo %s > %s \n" % (input_file, input_list)
    cmd = "./HggApp %s %s %s \n" % (input_list, outputfile, config)
    rmlist = "rm %s \n" % input_list
    commands.append([makelist,cmd,rmlist])

job = 0
file_counter = 0
cmds_per_job = int(len(commands)) / int(njobs) #integer division
bsub_cmds = []
bsub_file = None

#loop over all commands
print len(commands)
for ii in range(len(commands)):
	#make sure the extra jobs are added to the last file
    if (file_counter == 0) and (job != njobs):		
        bsub_file_name = output_dir+"/src/bsub_%i.src" % job
        bsub_file = open(bsub_file_name,"a")
        bsub_file.write('#!/bin/bash\n')
        bsub_file.write('#$ -S /bin/sh \n')
        bsub_file.write("cd /home/jhardenbrook/2013/RAZOR_DIPHOTON/HggApp_Razor/CMSSW_6_2_0\n")
        bsub_file.write("export SCRAM_ARCH=slc5_amd64_gcc462 \n")
        bsub_file.write("export HADOOP_CONF_DIR=/etc/hadoop \n")
        bsub_file.write("eval `scramv1 ru -sh`\n")
        bsub_file.write("cd .. \n")

        queue = "all.q@compute-2-4.local,all.q@compute-3-2.local,all.q@compute-3-7.local,all.q@compute-3-8.local"
        logarea = output_dir +"/logs/"
        cmd= "qsub -o %s -e %s -q %s %s" % (logarea,logarea, queue, bsub_file_name)

        bsub_cmds.append(cmd)

		#increment the counter
        job+=1

    bsub_file.write(commands[ii][0])
    bsub_file.write(commands[ii][1])
    bsub_file.write(commands[ii][2])
    
    if file_counter == cmds_per_job:
        file_counter = 0		
    elif job == njobs:
        continue
    else:
        file_counter+=1

#print out the submission commands
for ii in bsub_cmds:print ii
	

