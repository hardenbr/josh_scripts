import sys, os

def print_usage():
    print "Usage: python move_to_castor.py [DIR OF FILES TO MOVE] [NAME_OF_FOLDER_CASTOR] [PRINT(0) or EXECUTE(1)]"

if len(sys.argv) != 4:
    print_usage()
    exit(1)
    
_dir_from = sys.argv[1]
_dir_to = sys.argv[2]

current_dir = os.getcwd()
castor_dir = "/castor/cern.ch/user/h/hardenbr/" + sys.argv[2]

print "leaving directory"
os.chdir(_dir_from)
files = os.listdir(os.getcwd())

if int(sys.argv[3]) == 0:
    print "Making Directory: " + castor_dir
else:
    print "Making Directory: " + castor_dir
    os.system("rfmkdir " + castor_dir)

for f in files:
    command = "rfcp " + f + " " + castor_dir
    if int(sys.argv[3]) == 0:
        print command
    else:
        os.system("rfcp " + f + " " + castor_dir)

print "returning to original directory"
os.chdir(current_dir)
