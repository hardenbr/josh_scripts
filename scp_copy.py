import os, sys

if len(sys.argv) == 1:
    print "usage: scp_move.py [LIST_OF_PLOTS_TO_MOVE]"
    exit(1)
    
os.system("rm ~/SCP_PLOTS/*")

for ii in sys.argv[1:]:
    cmd = "cp " + ii + " ~/SCP_PLOTS"
    print cmd
    os.system(cmd)

