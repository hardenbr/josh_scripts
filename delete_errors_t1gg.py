import os, sys

dir = "$WSPACE/MC/T1GG"
cmd = "grep Error *  -i | grep -v Branch -i  |  awk '{FS=\".log\"; print $1}' > temp"
os.system(cmd)

fin = open("temp")
lines = fin.readlines()
lines_fix = map(lambda(x):x.rstrip("\n"),lines)

lines_fix[0] = lines_fix[0][:-13]

for ii in lines_fix:
    print "rfrm " + dir + "/" +  ii + ".root"
    print "rm " + ii + ".log"

os.system("rm temp")
