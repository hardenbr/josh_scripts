##Generates config files, and batch submission batch.src files with appropriate directories
#you must have a text file with a list of finished jobs

import sys, os


noptargs = 6
nargs = 5
n_passed = len(sys.argv)-1
if n_passed != nargs and n_passed != noptargs:
    print "usage python bit_tree_combiner_bsub.py <mass_trigger_tree_dir> <no_mass_trigger_tree_dir> <mass_hipt_trigger_tree_dir> <NJOBS> <OUTPUT_DIR> <FORCE_REMOVE=1>" 
    exit(1)



tree_mass_dir = sys.argv[1]
tree_no_mass_dir = sys.argv[2]
tree_mass_hipt_dir = sys.argv[3]
njobs = int(sys.argv[4])
output_dir = sys.argv[5]
force_remove = int(sys.argv[4])

if force_remove:
    os.system("rm -r " + output_dir)


list_mass_trees = os.listdir(tree_mass_dir)
list_no_mass_trees = os.listdir(tree_no_mass_dir)
list_mass_hipt_trees = os.listdir(tree_mass_hipt_dir)

tree_list = []
for ii in list_mass_trees:
    if "tree" not in ii: continue    
    for jj in list_no_mass_trees:        
        if "tree" not in jj: continue
        #if we are doing a third trigger
        for kk in list_mass_hipt_trees:
            if "tree" not in kk: continue                

            tree_list.append([ii,jj,kk])


ntrees_comb = len(tree_list)

print "NTREES:",  ntrees_comb

trees_per_job = ntrees_comb / njobs


#build the directories
os.system("mkdir " + output_dir)
os.system("mkdir " + output_dir+"/logs")
os.system("mkdir " + output_dir+"/src")
os.system("mkdir " + output_dir+"/res")


commands = []
counter = 0 

for ii in range(njobs):
	begin = counter
	end = counter + trees_per_job
	counter+= trees_per_job
	if ii == njobs-1:
		end = ntrees_comb
	
	cmd = "python ~/josh_scripts/bit_tree_combiner.py %s %s %s %i %i" % (tree_mass_dir, tree_no_mass_dir, tree_mass_hipt_dir, begin, end)

	commands.append(cmd)

#write the bsub commands
job = 0
file_counter = 0
cmds_per_job = int(len(commands)) / int(njobs) #integer division

print "COMMANDS PER JOB:", cmds_per_job
bsub_cmds = []
bsub_file = None

#loop over all commands
for ii in range(len(commands)):
	#make sure the extra jobs are added to the last file
	if (file_counter == 0) and (job != njobs):		
		#write a new job
		bsub_file_name = output_dir+"/src/bsub_%i.src" % job
		bsub_file = open(bsub_file_name,"a")
		bsub_file.write('#!/bin/bash\n')
		bsub_file.write("cd /afs/cern.ch/user/h/hardenbr/2013/HIGGS_DIPHOTON_HLT/NEW_OPEN_HLT/CMSSW_5_2_8_patch1/src\n")
		bsub_file.write("export SCRAM_ARCH=slc5_amd64_gcc462 \n")
		bsub_file.write("eval `scramv1 ru -sh`\n")
                bsub_file.write("cd /afs/cern.ch/work/h/hardenbr/2013/HIGGS_DIPHOTON_HLT\n")

		cmd="bsub -q 1nd "
		cmd+= "-o %s/logs/job_%i.log " % (output_dir ,job)
		cmd+="source "+ bsub_file_name

		bsub_cmds.append(cmd)

		#increment the counter
		job+=1

	bsub_file.write(commands[ii])

	
	#if we are at the number of commands per job reset the counter
	file_counter+=1
	if file_counter == cmds_per_job:file_counter = 0		
	if job == njobs:
		continue

#print out the submission commands
for ii in bsub_cmds:print ii
	
