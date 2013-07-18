import os,sys,math

if len(sys.argv) != 2:
    print "usage cfg_maker.py [NAME_OF_CFG]"

cfg_name = sys.argv[1]

#FAKE AND SIGNAL REGIONS

var_MR = "MR[250.,225.,1200.]"
var_Rsq = "Rsq[.04,.03,.35]"

FULL_MR = "MR_FULL[225.,1200.]"
FULL_Rsq = "Rsq_FULL[.03,.35]"

fR1_MR  = "MR_fR1[225.,450.]"
fR1_Rsq = "Rsq_fR1[.03,.05]"

fR2_MR  = "MR_fR2[225.,300.]"
fR2_Rsq = "Rsq_fR2[.05,.14]"

fR3_MR  = "MR_fR3[225.,250.]"
fR3_Rsq = "Rsq_fR3[.07,.25]"

sR1_MR  = "MR_sR1[400.,1200.]"
sR1_Rsq = "Rsq_sR1[.03,.05]"

sR2_MR = "MR_sR2[300.,1200.]"
sR2_Rsq ="Rsq_sR2[.05,.14]"

sR3_MR = "MR_sR3[250.,1200.]"
sR3_Rsq = "Rsq_sR3[.14,.25]"

sR4_MR = "MR_sR4[225.,1200.]"
sR4_Rsq = "Rsq_sR4[.25,.35]"


#FIT PARAMETERS

mr0_1 = "MR01st_QCD[33,0,200]"
mr0_1s = "MR01st_QCD_s[41]"

r0_1 = "R01st_QCD[-.0507, -.1, 0]"
r0_1s = "R01st_QCD_s[.0183]"

mr0_2 = "MR02nd_QCD[150,0,150]"
mr0_2s = "MR02nd_QCD_s[3.75]"

r0_2 = "R02nd_QCD[-6.27e-09,-.1,0]"
r0_2s = "R02nd_QCD_s[.00554]"

b_1 = "b1st_QCD[.250,.22,.4]"
b_1s = "b1st_QCD_s[.052]"

b_2 = "b2nd_QCD[.13,.07,.18]"
b_2s = "b2nd_QCD_s[.028]"

lumi = "Lumi[4600]"

ntot = "Ntot_QCD[1300,1100,1400]"

f2 = "f2_QCD[.0331,.001,.3]"
f2s = "f2_QCD_s[.0125]"


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
