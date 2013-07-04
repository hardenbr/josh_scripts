##Generates config files, and batch submission batch.src files with appropriate directories
##"usage ohlt_config_maker.py <list_of_reco.txt> <list_of_raw.txt> <basic_config_cfg.py>"

from tempfile import mkstemp
from shutil import move
from os import remove, close
import sys

def replace(file_path, pattern, subst):
        #Create temp file
        fh, abs_path = mkstemp()
        new_file = open(abs_path,'w')
        old_file = open(file_path)
        for line in old_file:
            new_file.write(line.replace(pattern, subst))
            #close temp file
            new_file.close()
            close(fh)
            old_file.close()
            #Remove original file
            remove(file_path)
            #Move new file
            move(abs_path, file_path)

if len(sys.argv) != 5:
	print "usage ohlt_config_maker.py <list_of_reco.txt> <list_of_raw.txt> <basic_config_cfg.py> <output_dir>"

pwd = os.getenv("PWD")
output_dir = sys.argv[4]

#OPEN THE FILES
reco = open(sys.argv[1],"r")
raw = open(sys.argv[2],"r")
cfg = open(sys.argv[3],"r")
#READ THE LINES IN
reco_lines = reco.readlines()
raw_lines = reco.readlines()
#Count how many config files we will need
n_reco = len(reco_lines)


for ii in range(n_reco):

