import os, sys

if(len(sys.argv) != 2):
    print "usage: stage_castor.py [CASTOR_DIR_NAME]"
    exit(1)

stage_folder = sys.argv[1]

stage_list = open("stage_list.temp","write")

cmd = "nsls " + stage_folder + " "
cmd += " | awk '{ print \"/castor/cern.ch/user/h/hardenbr/"+stage_folder+"/\"$1}'"
cmd += " > stage_list.temp"

os.system(cmd)

os.system("stager_get -f stage_list.temp")

os.system("rm stage_list.temp")
