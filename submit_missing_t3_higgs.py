import sys,os

wd = "/home/jhardenbrook/2013/RAZOR_DIPHOTON/HggApp_Razor"
queue = "all.q@compute-2-4.local,all.q@compute-3-2.local,all.q@compute-3-7.local,all.q@compute-3-8.local"
def build_cmd(num, dir):
    cmd = "qsub -o %s/%s/log" % (wd,dir)
    cmd += " -e %s/%s/log/ -q %s" % (wd,dir,queue)
    cmd += " " + dir + "/src/submit_" + num + ".src "
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
