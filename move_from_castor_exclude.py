import os,sys

if len(sys.argv) != 2:
    print "usage: ./move_from_castor.py [CASTOR_DIR_NAME]"
    exit(1)

f_name = sys.argv[1]
finished = os.listdir(os.getcwd())

os.system("nsls " + str(f_name) + "> files.temp")

f_move = open("files.temp")

flist = f_move.readlines()

flist_2 = map(lambda(x):x.rstrip("\n"),flist)

for ii in flist_2:
    cmd = "rfcp $CPATH/" + str(f_name) + "/" + ii + " ."
    if ii not in finished:
        os.system("echo " + ii + ";" + cmd)
        #print "echo " + ii
        #print cmd

os.system("rm files.temp")
