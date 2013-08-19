##Generates config files, and batch submission batch.src files with appropriate directories
#you must have a text file with a list of finished jobs

import sys, os
#print usage message
if len(sys.argv) != 8 and len(sys.argv) != 9:
	print "usage filter_new_ohlt_config_maker.py <pmin> <pmax> <hlt.cfg> <full_path_to_output_dir> <njobs> <force_remove=1> <new_bit_name> <max_splitting> <finished_jobs.txt OPTIONAL>"
        exit(1)

pwd = os.getenv("PWD")
output_dir = sys.argv[4]
hlt_name = sys.argv[3]

pmin = int(sys.argv[1])
pmax = int(sys.argv[2])
njobs = int(sys.argv[5])
force_remove = int(sys.argv[6])
new_bit_name = sys.argv[7]
max_splitting = int(sys.argv[8])

finished_jobs = None
finished_lines = None
finished_points = []

#in the optiona case of finished lines
if len(sys.argv) == 10:
	finished_jobs = open(sys.argv[9], "r")
	finished_lines = finished_jobs.readlines()

        #parse out the finished points in the txt file

	for ii in finished_lines:
		split = ii.split()
		lead = int(split[3])
		sublead = int(split[4])
		finished_points.append([lead,sublead])

#remove old instances of the output directory

if(force_remove): os.system("rm -r " + output_dir)
else: os.system("rm -ri " + output_dir)
#build the directories
os.system("mkdir " + output_dir)
os.system("mkdir " + output_dir+"/logs")
os.system("mkdir " + output_dir+"/src")
os.system("mkdir " + output_dir+"/hlts")
os.system("mkdir " + output_dir+"/res")


commands = []
#HLT_bit = "HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2"
#HLT_bit = "HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6"
HLT_bit = "HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1"
mass = 80

#generate the commands pathmaker_cmd and filter_cmd
for px in range(pmin,pmax):
	for py in range(pmin,px):
		if [px,py] in finished_points: continue

		if abs(px-py) < max_splitting: continue 
		

		i_menu = hlt_name
		o_menu = "hlt_%i_%i.py" % (px, py)
		o_menu_dir = output_dir+"hlts/"+o_menu
		c_flag = "changed_lead_%i_sublead_%i_mass%i" % (px,py,mass)
		
		
		#path change for NO MASS trigger
		#pathmaker_cmd = "python path_maker.py -i %s -o %s -p %s -c \"hltEG36EtFilter.etcutEB = cms.double( %i.0 )\" \"hltEG36EtFilter.etcutEE = cms.double( %i.0 )\" \"hltEG22EtDoubleFilterUnseeded.etcutEB = cms.double( %i.0 )\" \"hltEG22EtDoubleFilterUnseeded.etcutEE = cms.double( %i.0 )\" -r \"%s\"\n" % (i_menu, o_menu, HLT_bit, px, px, py, py, c_flag)

		#path change for MASS70 trigger
		#pathmaker_cmd = "python path_maker.py -i %s -o %s -p %s -c \"hltEG26EtFilter.etcutEB = cms.double( %i.0 )\" \"hltEG26EtFilter.etcutEE = cms.double( %i.0 )\" \"hltEG18EtDoubleFilterUnseeded.etcutEB = cms.double( %i.0 )\" \"hltEG18EtDoubleFilterUnseeded.etcutEE = cms.double( %i.0 )\" -r \"%s\"\n" % (i_menu, o_menu, HLT_bit, px, px, py, py, c_flag)

		#path change for MASS80 HI PT trigger
		pathmaker_cmd = "python path_maker.py -i %s -o %s -p %s -c \"hltEG36EtFilter.etcutEB = cms.double( %i.0 )\" \"hltEG36EtFilter.etcutEE = cms.double( %i.0 )\" \"hltEG10EtDoubleFilterUnseeded.etcutEB = cms.double( %i.0 )\" \"hltEG10EtDoubleFilterUnseeded.etcutEE = cms.double( %i.0 )\" -r \"%s\"\n" % (i_menu, o_menu, HLT_bit, px, px, py, py, c_flag)


		prod_file = "/afs/cern.ch/work/h/hardenbr/2013/HIGGS_DIPHOTON_HLT/RUN_208390_2012D_hgg2012_threetriggers/res/ohlt_output_0.root"

		#name of the output file we dont really need from the filter
		out_file = output_dir+"/res/temp_%i_%i.root" % (px, py)
		go_file = "go_%s_%s.py" % (px, py)
		log_file = output_dir + "logs/log_%s_%s" % (px, py)
		#comand to perform the actual filtering
		filter_cmd = "python openHLT.py -i %s -o %s -t %s -n -1 -g %s --go \n" %(prod_file, out_file, o_menu, go_file)			   

		tree_file = output_dir+"/res/tree_%i_%i.root" % (px, py)
		tree_cmd = "python ~/josh_scripts/make_bit_tree.py %i %i %s %s %s %i %s \n" % (px, py, out_file, tree_file, HLT_bit, mass, new_bit_name)

		#clean up the hlt files made, and unnecessary output file 
		cleanup_cmd = "rm %s %sc %s %s\n" % (o_menu, o_menu, out_file, go_file)

		commands.append([pathmaker_cmd,filter_cmd,tree_cmd,cleanup_cmd])

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
	bsub_file.write(commands[ii][3])
	
	#if we are at the number of commands per job reset the counter
	file_counter+=1
	if file_counter == cmds_per_job:file_counter = 0		
	if job == njobs:
		continue

#print out the submission commands
for ii in bsub_cmds:print ii
	
