import sys, os
import ROOT as rt

if len(sys.argv) != 2:
    print "usage mr_rsq.py [ROOT_FILE]"

os.system("root " + sys.argv[1] + " -c ~/josh_scripts/helper_fit_output.C -l -b")
