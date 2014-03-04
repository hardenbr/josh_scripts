import sys, os
import ROOT as rt

#THINGS TO CHANGE:
#1. RAW RATE FOR THE UNALTERED TRIGGER
#2. THE NUMBER OF EVENTS THE NOMINAL TRIGGER PASSES (RAW)
#3. NAME OF THE BIT TO BE RETRIEVED FROM THE TREE FILE
#4. THE NAME OF THE BIT BEING PULLED FROM THE BRANCH


noptargs = 5
nargs = 4
n_passed = len(sys.argv)-1
if n_passed != nargs and n_passed != noptargs:
    print "usage python bit_tree_combiner.py <BEGIN_COUNTER> <END_COUNTER> <mass_trigger_tree_dir> <no_mass_trigger_tree_dir> <mass_hipt_trigger_tree_dir OPTIONAL> " 
    exit(1)

raw_rate_mass = 18.32
raw_rate_nomass = 11.16#18.32
raw_rate_mass_hipt = 17.36

nominal_lumi = 6e33

nominal_pass_mass = 5563.
nominal_pass_nomass = 3416.
nominal_pass_mass_hipt = 5264.

do_third = False

tree_mass_dir = sys.argv[3]
tree_no_mass_dir = sys.argv[4]
tree_mass_hipt_dir = ""

start_counter = int(sys.argv[1])
end_counter = int(sys.argv[2])

mass_bit_name = "hlt_mass_scan"#"hlt_mass100_scan"
no_mass_bit_name = "hlt_nomass_scan"#"hlt_mass100_scan"
mass_hipt_bit_name = "hlt_mass_hipt_scan"

list_mass_trees = os.listdir(tree_mass_dir)
list_no_mass_trees = os.listdir(tree_no_mass_dir)
list_mass_hipt_trees = []

if do_third:
    tree_mass_hipt_dir = sys.argv[5]
    list_mass_hipt_trees = os.listdir(tree_mass_hipt_dir)

print "----------------------------------------------------------"
if do_third:
    print "COUNTER NEVENTS N_PASS|  MASS_PX MASS_PY MASS_NUNIQ MASS_RAW |  NOMASS_PX NOMASS_PY NOMASS_NUNIQ NO_MASS_RAW | MASS_HIPT_PX MASS_HIPT_PY MASS_HIPT_NPASS MASS_HIPT_RAW | NMASS_NOMASS N_MASS_HIPT  NOMASS_HIPT | N_ALLFIRE N_NOFIRE"
else:
    print "nominal pass mass, rate:",mass_bit_name, nominal_pass_mass
    print "nominal pass nomass, rate:", no_mass_bit_name, nominal_pass_nomass
    print "nominal lumi:", nominal_lumi


    print "COUNTER NEVENTS N_PASS|  MASS_PX MASS_PY MASS_NUNIQ MASS_RAW |  NOMASS_PX NOMASS_PY NOMASS_NUNIQ NO_MASS_RAW | N_ALLFIRE N_NOFIRE | TOTAL_RATE"
print "----------------------------------------------------------"

tree_list = []
for ii in list_mass_trees:
    if "tree" not in ii: continue    
    for jj in list_no_mass_trees:        
        if "tree" not in jj: continue
        #if we are doing a third trigger
        if do_third:        
            for kk in list_mass_hipt_trees:
                if "tree" not in kk: continue                
                tree_list.append([ii,jj,kk])
        else:
            tree_list.append([ii,jj])

counter = 0 
for ii in tree_list:

    if counter < start_counter:
        counter+=1
        continue 
    elif counter > end_counter:
        counter+=1
        continue
    else:
        counter+=1
        
    ii_x = int(ii[0].split("_")[1])
    ii_y = int(ii[0].split("_")[2][:-5])
    
    jj_x = int(ii[1].split("_")[1])
    jj_y = int(ii[1].split("_")[2][:-5])

#    if ii_x != 26 or ii_y != 18 or jj_x != 36 or jj_y != 22: continue

    kk_x = 0
    kk_y = 0

    #GRAB THE FILES
    mass_file = rt.TFile(tree_mass_dir +"/"+ii[0])
    no_mass_file = rt.TFile(tree_no_mass_dir + "/"+ ii[1])
    mass_hipt_file = None
    
    #GET THE TREES
    mass_tree = mass_file.Get("myTree")
    no_mass_tree = no_mass_file.Get("myTree")
    mass_hipt_tree = None

    #Activate the entries
    mass_tree.SetBranchStatus(mass_bit_name,1)
    no_mass_tree.SetBranchStatus(no_mass_bit_name,1)
    mass_tree.SetBranchStatus("counter",1)
    no_mass_tree.SetBranchStatus("counter",1)

    #FILL THE BITS FROM THE TREES
    hlt_bit_mass = []
    hlt_bit_no_mass = []
    hlt_bit_mass_hipt = []
    
    #PARSE OUT THE BITS
    nentries = mass_tree.GetEntries()
    for entry in range(nentries):
        mass_tree.GetEntry(entry)
        no_mass_tree.GetEntry(entry)

        hlt_bit_mass.append(mass_tree.hlt_mass_scan)
        #hlt_bit_no_mass.append(no_mass_tree.hlt_mass100_scan)
        hlt_bit_no_mass.append(no_mass_tree.hlt_nomass_scan)

        #IF WE ARENT DOING THE THIRD LET IT NEVER TRIGGER
        if not do_third:
            hlt_bit_mass_hipt.append(0)

    #IF WE WANT TO INCLUDE THE THIRD TRIGGER
    if do_third:
        kk_x = int(ii[2].split("_")[1])
        kk_y = int(ii[2].split("_")[2][:-5])

        mass_hipt_file = rt.TFile(tree_mass_hipt_dir+"/"+ii[2])    
        mass_hipt_tree = mass_hipt_file.Get("myTree")

        mass_hipt_tree.SetBranchStatus(mass_hipt_bit_name,1)

        for entry in range(nentries):
            mass_hipt_tree.GetEntry(entry)            
            hlt_bit_mass_hipt.append(mass_hipt_tree.hlt_mass_hipt_scan)   
        
    #CALCULATE THE UNIQUE RATES
    uniq_mass_bits = 0
    uniq_no_mass_bits = 0
    uniq_mass_hipt_bits = 0

    raw_mass_bits = 0
    raw_no_mass_bits = 0
    raw_mass_hipt_bits = 0

    mass_hipt = 0
    mass_nomass = 0
    nomass_hipt = 0

    all = 0
    none = 0
    
    for ii in range(len(hlt_bit_mass)):

        #CALCULATE THE UNIQUE LOGIC
        uniq_mass = hlt_bit_mass[ii] and not hlt_bit_no_mass[ii] and not hlt_bit_mass_hipt[ii]
        uniq_no_mass = not hlt_bit_mass[ii] and hlt_bit_no_mass[ii] and not hlt_bit_mass_hipt[ii]
        uniq_mass_hipt = False

        #CALCULATE THE TWO FIRE LOGIC

        two_mass_nomass = hlt_bit_mass[ii] and hlt_bit_no_mass[ii] and not hlt_bit_mass_hipt[ii]
        two_mass_hipt = False
        two_nomass_hipt = False
        three_all = False
        
        
        if do_third:
            uniq_mass_hipt = not hlt_bit_mass[ii] and not hlt_bit_no_mass[ii] and hlt_bit_mass_hipt[ii] 
            two_mass_hipt = hlt_bit_mass[ii] and not hlt_bit_no_mass[ii] and hlt_bit_mass_hipt[ii]
            two_nomass_hipt = not hlt_bit_mass[ii] and hlt_bit_no_mass[ii] and hlt_bit_mass_hipt[ii]
            three_all = hlt_bit_mass[ii] and hlt_bit_no_mass[ii] and hlt_bit_mass_hipt[ii]


        #INCREMENT THE RAW COUNTS
        if hlt_bit_mass[ii]: raw_mass_bits+=1
        if hlt_bit_no_mass[ii]: raw_no_mass_bits+=1
        if hlt_bit_mass_hipt[ii]: raw_mass_hipt_bits+=1

        #INCREMENT THE EVENT CLASSIFICATION
        if uniq_mass:uniq_mass_bits+=1
        elif uniq_no_mass: uniq_no_mass_bits+=1
        elif uniq_mass_hipt: uniq_mass_hipt_bits+=1
        elif two_nomass_hipt: nomass_hipt+=1
        elif two_mass_nomass: mass_nomass+=1
        elif two_mass_hipt: mass_hipt+=1
        elif three_all: all+=1
        else: none+=1


    rate_factor_mass = raw_rate_mass / nominal_pass_mass
    rate_factor_nomass = raw_rate_nomass / nominal_pass_nomass
    rate_factor_mass_hipt = 0

    average_rate = 0
    

    if do_third:
        rate_factor_mass_hipt = raw_rate_mass_hipt / nominal_pass_mass_hipt
        average_rate = (rate_factor_mass + rate_factor_nomass + rate_factor_mass_hipt) / 3.0
    else:
        average_rate = (rate_factor_mass + rate_factor_nomass) / 2.0 

    total_rate = average_rate *  float(len(hlt_bit_mass) - none) 
    
    if do_third:
        frac_uniq_mass_hipt = float(uniq_mass_hipt_bits) / float(raw_mass_hipt_bits)
        
    if do_third:
        print counter, len(hlt_bit_mass), all, "|",ii_x, ii_y, uniq_mass_bits, raw_mass_bits,"|", jj_x, jj_y, uniq_no_mass_bits, raw_no_mass_bits,"|", kk_x, kk_y, uniq_mass_hipt_bits, raw_mass_hipt_bits, "|", mass_nomass, mass_hipt, nomass_hipt, "|", all, none, "|", total_rate

    else:
        print counter, len(hlt_bit_mass), all, "|",ii_x, ii_y, uniq_mass_bits, raw_mass_bits,"|", jj_x, jj_y, uniq_no_mass_bits, raw_no_mass_bits,"|", mass_nomass, none, "|", total_rate        
            
