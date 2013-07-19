##Generates config files, and batch submission batch.src files with appropriate directories
##"usage ohlt_config_maker.py <list_of_reco.txt> <list_of_raw.txt> <basic_config_cfg.py>"
##You must place the appropriate replace strings in the config file

import sys, os
#print usage message
if len(sys.argv) != 6:
	print "usage filter_new_ohlt_config_maker.py <pmin> <pmax> <hlt.cfg> <full_path_to_output_dir> <njobs>"
        exit(1)

#get some names and paths
pwd = os.getenv("PWD")
output_dir = sys.argv[4]
hlt_name = sys.argv[3]

#OPEN THE FILES
pmin = int(sys.argv[1])
pmax = int(sys.argv[2])
njobs = int(sys.argv[5])
#READ THE LINES IN

#remove old instances of the output directory
os.system("rm -ri " + output_dir)
#build the directories
os.system("mkdir " + output_dir)
os.system("mkdir " + output_dir+"/logs")
os.system("mkdir " + output_dir+"/src")
os.system("mkdir " + output_dir+"/hlts")
os.system("mkdir " + output_dir+"/res")


commands = []
#generate the commands pathmaker_cmd and filter_cmd
for px in range(pmin,pmax):
	for py in range(pmin,px):		
		HLT_bit = "HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2"
		i_menu = hlt_name
		o_menu = "hlt_%i_%i.py" % (px, py)
		o_menu_dir = output_dir+"hlts/"+o_menu
		c_flag = "changed_lead_%i_sublead_%i" % (px,py)
		
		#command for the pathmaking script
		pathmaker_cmd = "python path_maker.py -i %s -o %s -p %s -c \"hltEG26EtFilter.etcutEB = cms.double( %i.0 )\" \"hltEG26EtFilter.etcutEE = cms.double( %i.0 )\" \"hltEG18EtDoubleFilterUnseeded.etcutEB = cms.double( %i.0 )\" \"hltEG18EtDoubleFilterUnseeded.etcutEE = cms.double( %i.0 )\" -r \"%s\"\n" % (i_menu, o_menu, HLT_bit, px, px, py, py, c_flag)

		prod_file = "/afs/cern.ch/work/h/hardenbr/2013/HIGGS_DIPHOTON_HLT/RUN_208390_2012D_MASS_CUT/res/ohlt_output_1.root"

		#name of the output file we dont really need from the filter
		out_file = output_dir+"res/temp_%i_%i.root" % (px, py)
		go_file = "go_%s_%s.py" % (px, py)
		log_file = output_dir + "logs/log_%s_%s" % (px, py)
		#comand to perform the actual filtering
		filter_cmd = "python openHLT.py -i %s -o %s -t %s -n -1 -g %s --go \n" %(prod_file, out_file, o_menu, go_file)			   

		#clean up the hlt files made, and unnecessary output file 
		cleanup_cmd = "rm %s %sc %s %s\n" % (o_menu, o_menu, out_file, go_file)

		commands.append([pathmaker_cmd,filter_cmd,cleanup_cmd])

#write the bsub commands
job = 0
file_counter = 0
cmds_per_job = int(len(commands)) / int(njobs) #integer division
bsub_cmds = []
bsub_file = None

#loop over all commands
for ii in range(len(commands)):
	#make sure the extra jobs are added to the last file
	if (file_counter == 0) and (job != njobs):		
		#write a new job
		bsub_file_name = output_dir+"/src/bsub_%i.src" % job
		bsub_file = open(bsub_file_name,"a")
		bsub_file.write('#!/bin/bash\n')
		bsub_file.write("cd /afs/cern.ch/user/h/hardenbr/2013/HIGGS_DIPHOTON_HLT/NEW_OPEN_HLT/CMSSW_5_2_8_patch1/src\n")
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
	
