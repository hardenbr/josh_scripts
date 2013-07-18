import os,sys,math

if len(sys.argv) != 2:
    print "usage cfg_maker.py [NAME_OF_CFG]"

cfg_name = sys.argv[1]

#FAKE AND SIGNAL REGIONS

var_MR = "MR[120.,160.,3000.]"
var_Rsq = "Rsq[.06,.03,1.2]"

FULL_MR = "MR_FULL[160.,3000.]"
FULL_Rsq = "Rsq_FULL[.03,1.2]"

fR1_MR  = "MR_fR1[225.,400.]"
fR1_Rsq = "Rsq_fR1[.03,.05]"

fR2_MR  = "MR_fR2[225.,350.]"
fR2_Rsq = "Rsq_fR2[.05,.14]"

fR3_MR  = "MR_fR3[225.,275.]"
fR3_Rsq = "Rsq_fR3[.07,.35]"

sR1_MR  = "MR_sR1[400.,3000.]"
sR1_Rsq = "Rsq_sR1[.03,.05]"

sR2_MR = "MR_sR2[350.,3000.]"
sR2_Rsq ="Rsq_sR2[.05,.14]"

sR3_MR = "MR_sR3[275.,3000.]"
sR3_Rsq = "Rsq_sR3[.14,.35]"

sR4_MR = "MR_sR4[225.,3000.]"
sR4_Rsq = "Rsq_sR4[.35,.65]"


#FIT PARAMETERS

mr0_1 = "MR01st_QCD[22.9,0,200]"
mr0_1s = "MR01st_QCD_s[25.5]"

mr0_2 = "MR02nd_QCD[-95.5,-300,300]"
mr0_2s = "MR02nd_QCD_s[54]"

ntot = "Ntot_QCD[5500,2000,10000]"

r0_1 = "R01st_QCD[-.04664, -.1, 0]"
r0_1s = "R01st_QCD_s[.0179]"

r0_2 = "R02nd_QCD[-.237,-1,0]"
r0_2s = "R02nd_QCD_s[.0586]"

b_1 = "b1st_QCD[2.59,.5,10]"
b_1s = "b1st_QCD_s[.733]"

b_2 = "b2nd_QCD[.192,.1,100]"
b_2s = "b2nd_QCD_s[.2]"

f2 = "f2_QCD[.2,.0001,.5]"
f2s = "f2_QCD_s[.0132]"

lumi = "Lumi[4600]"




#var_ranges = [FULL_MR, FULL_Rsq, fR1_MR, fR1_Rsq, fR2_MR, fR2_Rsq, fR3_MR, fR3_Rsq]
var_ranges = [FULL_MR, FULL_Rsq, fR1_MR, fR1_Rsq, fR2_MR, fR2_Rsq, fR3_MR, fR3_Rsq, sR1_MR, sR1_Rsq, sR2_MR, sR2_Rsq, sR3_MR, sR3_Rsq, sR4_MR, sR4_Rsq]

pdf1_qcd = [mr0_1,mr0_1s, r0_1, r0_1s, b_1, b_1s]
pdf2_qcd = [mr0_2,mr0_2s, r0_2, r0_2s, b_2, b_2s]
other_par = [lumi, ntot, f2, f2s]

fout = open(cfg_name,"w")

fout.write("[Had]\n")
fout.write("variables = ['" + var_MR + "','" + var_Rsq + "']\n")
fout.write("variables_range = [")

for ii in range(len(var_ranges)):
    if ii != len(var_ranges)-1:
        fout.write("'" + var_ranges[ii] + "',")
    else:
        fout.write("'" + var_ranges[ii] + "']\n")
        
fout.write("#QCD from control box\n")
        
fout.write("pdf1_QCD = [")

for ii in range(len(pdf1_qcd)):
    if ii != len(pdf1_qcd) - 1:
        fout.write("'" + pdf1_qcd[ii] + "',")
    else:
        fout.write("'" + pdf1_qcd[ii] + "']\n")

fout.write("pdf2_QCD =[")

for ii in range(len(pdf2_qcd)):
    if ii != len(pdf2_qcd) - 1:
        fout.write("'" + pdf2_qcd[ii] + "',")
    else:
        fout.write("'" + pdf2_qcd[ii] + "']\n")
                

fout.write("others_QCD = [")

for ii in range(len(other_par)):
    if ii != len(other_par) - 1:
        fout.write("'" + other_par[ii] + "',")
    else:
        fout.write("'" + other_par[ii] + "']\n")
