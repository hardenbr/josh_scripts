import os, sys

if len(sys.argv) != 2:
    print "usage python npeek.py (NUM_JOB)"
    exit(1)

os.system("qstat | grep ' r ' > running_temp.txt")
f = open("running_temp.txt")
f_lines = f.readlines()
for ii in range(len(f_lines)):
    if ii == int(sys.argv[1]):
        cmd = "qstat -j " + str(f_lines[ii].split(" ")[0])
        print cmd
        os.system(cmd)
os.system("rm running_temp.txt")        
    
