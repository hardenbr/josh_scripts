##Generates config files, and batch submission batch.src files with appropriate directories
##"usage ohlt_config_maker.py <list_of_reco.txt> <list_of_raw.txt> <basic_config_cfg.py>"
##You must place the appropriate replace strings in the config file

import sys, os
#print usage message
if len(sys.argv) != 4:
	print "usage new_ohlt_config_maker.py <list_of_raw.txt> <basic_config_cfg.py> <full_path_to_output_dir>"
        exit(1)

#get some names and paths
pwd = os.getenv("PWD")
output_dir = sys.argv[3]
cfg_name = sys.argv[2]

#OPEN THE FILES
raw = open(sys.argv[1],"r")
cfg = open(cfg_name,"r")
#READ THE LINES IN
#reco_lines = reco.readlines()
raw_lines = raw.readlines()

#Count how many config files we will need
#there better not be extra lines in the lists!
#n_reco = len(reco_lines)
n_raw = len(raw_lines)

#make the raw list we will be inserting
raw_list = ""
for ii in raw_lines:
        raw_list += "'"+ii.rstrip("\n")+"',\n"

raw_list=raw_list.rstrip(",\n")+"\n"

#remove old instances of the output directory
os.system("rm -r " + output_dir)
#build the directories
os.system("mkdir " + output_dir)
os.system("mkdir " + output_dir+"/cfgs")
os.system("mkdir " + output_dir+"/logs")
os.system("mkdir " + output_dir+"/src")
os.system("mkdir " + output_dir+"/res")

#strings to be replaced in the config file
#reco_replace_string = "#$REPLACE_RECO$#"
raw_replace_string = "#$REPLACE_RAW$#"
output_replace_string = "#$REPLACE_OUTPUT$#"

for ii in range(n_raw):
	#make the new cfg file	
        new_file_name = output_dir+"/cfgs/"+cfg_name.rstrip(".py")+"_"+str(ii)+".py"
        cfg_file = open(cfg_name, "r")
        cfg_file_lines = cfg_file.readlines()
        new_file = open(new_file_name,"a")
        #read all the lines of the old cfg file and replace the replace text
        for jj in range(len(cfg_file_lines)):
		#dont replace the reco for now (version is too old 53X)
                #if reco_replace_string in cfg_file_lines[jj]:
                #        cfg_file_lines[jj] = "'"+reco_lines[ii].rstrip("\n")+"'"
                if raw_replace_string in cfg_file_lines[jj]:
                        cfg_file_lines[jj] = cfg_file_lines[jj].replace(raw_replace_string,raw_lines[ii].rstrip("\n"))
                if output_replace_string in cfg_file_lines[jj]:
                        replace_string_out=output_dir+"/res/ohlt_output_"+str(ii)+".root" 
                        cfg_file_lines[jj] = cfg_file_lines[jj].replace(output_replace_string,replace_string_out)
        #write the cfg file
        new_file.writelines(cfg_file_lines)

        #now write the source files for bsub
        bsub_file_name = output_dir+"/src/"+"bsub_" + str(ii) + ".src"
        bsub_file = open(bsub_file_name,"a")
        bsub_file.write('#!/bin/bash\n')
	bsub_file.write("cd /afs/cern.ch/user/h/hardenbr/2013/HIGGS_DIPHOTON_HLT/NEW_OPEN_HLT/CMSSW_5_2_8_patch1/src\n")
	bsub_file.write("export SCRAM_ARCH=slc5_amd64_gcc462 \n")
	bsub_file.write("eval `scramv1 ru -sh`\n")	
        bsub_file.write("cmsRun " + new_file_name)

        #write out the commands
        cmd="bsub -q 1nd "
        cmd+= "-o " + output_dir + "/logs/log_" + str(ii) +".log "
        cmd+="source "+ bsub_file_name
                
        print cmd
