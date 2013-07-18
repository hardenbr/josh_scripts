##Generates config files, and batch submission batch.src files with appropriate directories
##"usage ohlt_config_maker.py <list_of_reco.txt> <list_of_raw.txt> <basic_config_cfg.py>"
##You must place the appropriate replace strings in the config file

import sys, os
#print usage message
if len(sys.argv) != 5:
	print "usage filter_new_ohlt_config_maker.py <pmin> <pmax> <hlt.cfg> <full_path_to_output_dir>"
        exit(1)

#get some names and paths
pwd = os.getenv("PWD")
output_dir = sys.argv[4]
hlt_name = sys.argv[3]

#OPEN THE FILES
pmin = int(sys.argv[1])
pmax = int(sys.argv[2])
#READ THE LINES IN

#remove old instances of the output directory
os.system("rm -r " + output_dir)
#build the directories
os.system("mkdir " + output_dir)
os.system("mkdir " + output_dir+"/logs")
os.system("mkdir " + output_dir+"/src")
os.system("mkdir " + output_dir+"/hlts")

for px in range(pmin,pmax):
	for py in range(pmin,px):		
		HLT_bit = "HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2"
		i_menu = hlt_name
		o_menu = "hlt_%i_%i.py" % (px, py)
		o_menu_dir = output_dir+"/hlts/"+o_menu
		c_flag = "changed_lead_%i_sublead_%i" % (px,py)
		
		#command for the pathmaking script
		pathmaker_cmd = "python path_maker.py -i %s -o %s -p %s -c \"hltEG26EtFilter.etcutEB = cms.double( %i.0 )\" \"hltEG26EtFilter.etcutEE = cms.double( %i.0 )\" \"hltEG18EtDoubleFilterUnseeded.etcutEB = cms.double( %i.0 )\" \"hltEG18EtDoubleFilterUnseeded.etcutEE = cms.double( %i.0 )\" -r \"%s\"\n" % (i_menu, o_menu_dir , HLT_bit, px, px, py, py, c_flag)

		prod_file = "/afs/cern.ch/work/h/hardenbr/2013/HIGGS_DIPHOTON_HLT/RUN_208390_2012D_MASS_CUT/res/ohlt_output_1.root"
		out_file = "/tmp/hardenbr/temp.root"

		#comand to perform the actual filtering
		filter_cmd = "python openHLT.py -i %s -o %s -t %s -n -1 --go\n" %(prod_file, out_file, o_menu)
			   
                #now write the source files for bsub
		bsub_file_name = output_dir+"/src/"+"bsub_"+str(px)+"_"+str(py)+".src"
		bsub_file = open(bsub_file_name,"a")
		bsub_file.write('#!/bin/bash\n')
		bsub_file.write("cd /afs/cern.ch/user/h/hardenbr/2013/HIGGS_DIPHOTON_HLT/NEW_OPEN_HLT/CMSSW_5_2_8_patch1/src\n")
		bsub_file.write("export SCRAM_ARCH=slc5_amd64_gcc462 \n")
		bsub_file.write("eval `scramv1 ru -sh`\n")
		bsub_file.write("cp %s . \n" % o_menu_dir)
		bsub_file.write(pathmaker_cmd)
		bsub_file.write(filter_cmd)
		bsub_file.write("rm %s \n" % o_menu)

                #write out the commands
		cmd="bsub -q 1nd "
		cmd+= "-o " + output_dir + "/logs/log_"+str(px)+"_"+str(py)+".log "
		cmd+="source "+ bsub_file_name
                
		print cmd
