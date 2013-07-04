import os, sys
dir = "BLUE_PLOT_TOYS"
basestring = "frtoydata_Had_"

append_list = []
had_group = 0

for ii in range(3500):

    append_list.append(basestring + str(ii) + ".root")

    if((ii != 0) & ((ii % 200) == 0)):
        command = "hadd toy_"+str(had_group)+".root "
        for ff in append_list:
            command += dir+"/"+ff + " "
        print command
        had_group+=1
        append_list = []
