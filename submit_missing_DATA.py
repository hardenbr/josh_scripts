import sys,os
import josh_functions as josh

def build_cmd(num, castor_dir):
    cmd = "bsub -q 1nd -o Data7TeV/"
    cmd += castor_dir + "/log/" + castor_dir + "_" + num + ".log "
    cmd += "source /afs/cern.ch/user/h/hardenbr/scratch0/CMSSW_4_2_7/src/VecBosApp/Data7TeV/" + castor_dir + "/src/submit_" + num + ".src "
    cmd += "-copyInput=Data7TeV_" + num
    return cmd

if len(sys.argv) != 3:
    print "Usage: python unfinish_DATA_v3 [CASTOR_DIR] [NUM_FILES]"
    exit(1)

castor_dir = sys.argv[1]
num_files = int(sys.argv[2])
os.system("ls $WSPACE/DATA/RA3/" + castor_dir + " > finished.temp")

flist = open("finished.temp").readlines()
#current_dir = os.getcwd()
done = map(lambda(x):x.rstrip("\n"),flist)

for ii in range(num_files):
    doprint = True
    for jj in done:
        if "_" + str(ii) + "."  in jj:
            doprint = False
    if doprint:
        print build_cmd(str(ii), castor_dir) + ";sleep 2"
    

os.system("rm finished.temp")
