import ROOT, numpy
from DataFormats.FWLite import Events, Handle
import os, sys
import ROOT as rt
nargs = 4

if len(sys.argv) != nargs+1:
    print "usage make_bit_tree.py <pt1> <pt2> <filter_output.root> <tree_output.root>"
    exit(1)

pt1 = int(sys.argv[1])
pt2 = int(sys.argv[2])
file = sys.argv[3]
tree_output = sys.argv[4]

variables = [["int","pt1"],["int","pt2"],["int","bit0"],["int","bit1"],["int","bit2"],["int","bit3"],["int","counter"]]

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
    if counter % 10000 == 0: print "Analyzing " + str(counter) + "..."


    event.getByLabel(input_tag, handle)

    trigres = handle.product()
    
    trignames = event.object().triggerNames(trigres)

    index_changed = trignames.triggerIndex("HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_changed_lead_23_sublead_22_mass0_v1") #2
    index_nomass = trignames.triggerIndex("HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6") #1
    index_mass = trignames.triggerIndex("HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass70_v2") #0

    setattr(s, "bit0", trigres[index_mass].accept())
    setattr(s, "bit1", trigres[index_nomass].accept())
    setattr(s, "bit2", trigres[index_changed].accept())
    setattr(s, "bit3", 0)
    setattr(s, "pt1" , pt1)
    setattr(s, "pt2" , pt2)
    setattr(s, "counter", counter)

    myTree.Fill()    

    counter+=1

fileOut = rt.TFile.Open(tree_output, "recreate")    
myTree.Write()
fileOut.Close()

os.system("rm " + macro_name)
