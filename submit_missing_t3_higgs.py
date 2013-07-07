import sys,os
import josh_functions as josh

def build_cmd(num, dir):
    cmd = "qsub -q 1nd -o " + 
    cmd += dir + "/log/"
    cmd += " -e " + dir + "/log/"
    cmd += " source /home/jhardenbrook/2013/RAZOR_DIPHOTON/HggApp_Razor/" + dir + "/src/submit_" + num + ".src "
    return cmd

if len(sys.argv) != 3:
    print "Usage: python unfinish_DATA_v3 [DIR] [NUM_FILES]"
    exit(1)

dir = sys.argv[1]
num_files = int(sys.argv[2])
os.system("ls /raid3/jhardenbrook/" + dir + " > finished.temp")

flist = open("finished.temp").readlines()
#current_dir = os.getcwd()
done = map(lambda(x):x.rstrip("\n"),flist)

for ii in range(num_files):
    doprint = True
    for jj in done:
        if "_" + str(ii) + "."  in jj:
            doprint = False
    if doprint:
        print build_cmd(str(ii), dir)
    

os.system("rm finished.temp")
