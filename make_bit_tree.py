import ROOT, numpy
from DataFormats.FWLite import Events, Handle
import os, sys
import ROOT as rt

nargs = 7

if len(sys.argv) != nargs+1:
    print "usage make_bit_tree.py <pt1> <pt2> <filter_output.root> <tree_output.root> <name_of_changed_bit> <mass> <new_bit_name>"
    exit(1)

pt1 = int(sys.argv[1])
pt2 = int(sys.argv[2])
file = sys.argv[3]
tree_output = sys.argv[4]
HLTBit = sys.argv[5]
mass = int(sys.argv[6])
new_bit_name = sys.argv[7]

variables = [["int","pt1"],["int","pt2"],["int","hlt_mass"],["int","hlt_nomass"],["int","hlt_mass_hipt"],["int",new_bit_name],["int","counter"],["int","mass"]]

stringStruct = "{\n\t struct thisStruct{\n \t"
for ii in variables:
    stringStruct+=ii[0]+" "+ii[1]+";\n\t"
stringStruct+="\t};\n}"

macro_name = "macro_%i_%i.C" % (pt1, pt2)

macro = open(macro_name, "w")
macro.write(stringStruct)
macro.close()

rt.gROOT.Macro(macro_name)
from ROOT import thisStruct

s = thisStruct()

myTree = rt.TTree("myTree", "myTree")

for ii in variables:
    varName = ii[1]
    branchName = ii[1]
    
    if ii[0] == "int":
        myTree.Branch(branchName, rt.AddressOf(s,varName),'%s/I' %varName)
    if ii[0] == "float":
        myTree.Branch(branchName, rt.AddressOf(s,varName),'%s/F' %varName)
        #    if ii[0] == "vector<float>":
        #        myTree.Branch(branchName, varName)
        
events = Events(file)

#handle = Handle('trigger::TriggerEvent')
#label = "hltTriggerSummaryAOD"

handle = Handle('edm::TriggerResults')
label = "TriggerResults"
process = "HLT3PB"

input_tag = (label,"",process)

ROOT.gROOT.SetBatch()
counter = 0

for event in events:    
    if counter % 1000 == 0: print "Analyzing " + str(counter) + "..."


    event.getByLabel(input_tag, handle)

    trigres = handle.product()
    
    trignames = event.object().triggerNames(trigres)

    changed_bit = HLTBit[:-3]+"_changed_lead_%i_sublead_%i_mass%i_v1" % (pt1, pt2, mass)

    index_changed = trignames.triggerIndex(changed_bit) #2
    index_nomass = trignames.triggerIndex("HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6") #1
    index_mass = trignames.triggerIndex("HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2") #0
    index_mass_highpt = trignames.triggerIndex("HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon10_R9Id85_OR_CaloId10_Iso50_Mass80_v1")

    setattr(s, "hlt_mass", trigres[index_mass].accept())
    setattr(s, "hlt_nomass", trigres[index_nomass].accept())
    setattr(s, "hlt_mass_hipt", trigres[index_mass_highpt].accept())
    setattr(s, new_bit_name, trigres[index_changed].accept())

    setattr(s, "pt1" , pt1)
    setattr(s, "pt2" , pt2)
    setattr(s, "mass", mass)
    setattr(s, "counter", counter)

    myTree.Fill()    

    counter+=1

fileOut = rt.TFile.Open(tree_output, "recreate")    
myTree.Write()
fileOut.Close()

os.system("rm " + macro_name)
