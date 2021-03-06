import os,sys,math

if len(sys.argv) != 2:
    print "usage cfg_maker.py [NAME_OF_CFG]"

cfg_name = sys.argv[1]

#FAKE AND SIGNAL REGIONS

var_MR = "MR[180,200.,3000.]"
var_Rsq = "Rsq[.06,.05,1.2]"

FULL_MR = "MR_FULL[200.,3000.]"
FULL_Rsq = "Rsq_FULL[.05,1.2]"

fR1_MR  = "MR_fR1[230.,500.]"
fR1_Rsq = "Rsq_fR1[.04,.06]"

fR2_MR  = "MR_fR2[230.,350.]"
fR2_Rsq = "Rsq_fR2[.05,.09]"

fR3_MR  = "MR_fR3[230,260.]"
fR3_Rsq = "Rsq_fR3[.09,.25]"

sR1_MR  = "MR_sR1[500.,3000.]"
sR1_Rsq = "Rsq_sR1[.05,.07]"

sR2_MR = "MR_sR2[225.,3000.]"
sR2_Rsq ="Rsq_sR2[.07,.14]"

sR3_MR = "MR_sR3[200.,3000.]"
sR3_Rsq = "Rsq_sR3[.14,.35]"

sR4_MR = "MR_sR4[160.,3000.]"
sR4_Rsq = "Rsq_sR4[.35,1.2]"


#FIT PARAMETERS

mr0_1 = "MR0_QCD[27.289,-200,200]"
mr0_1s = "MR0_QCD_s[23.7]"

#mr0_2 = "MR02nd_QCD[-8.27,-100,100]"
#mr0_2s = "MR02nd_QCD_s[24]"

ntot = "Ntot_QCD[15000,0,40000]"

r0_1 = "R0_QCD[-.046144, -.1, .1]"
r0_1s = "R0_QCD_s[.0172]"

#r0_2 = "R02nd_QCD[-.1,-.1,0]"
#r0_2s = "R02nd_QCD_s[.0206]"

b_1 = "b_QCD[5,0,50]"
b_1s = "b_QCD_s[.671]"

n_1 = "n_QCD[2.0989,0,10]"
n_1s = "n_QCD_s[.21]"

#b_2 = "b2nd_QCD[.085224,.05,.22]"
#b_2s = "b2nd_QCD_s[.0127]"

#f2 = "f2_QCD[.0434,.001,.4]"
#f2s = "f2_QCD_s[.0229]"

lumi = "Lumi[4600]"




#var_ranges = [FULL_MR, FULL_Rsq, fR1_MR, fR1_Rsq, fR2_MR, fR2_Rsq, fR3_MR, fR3_Rsq]
var_ranges = [FULL_MR, FULL_Rsq, fR1_MR, fR1_Rsq, fR2_MR, fR2_Rsq, fR3_MR, fR3_Rsq, sR1_MR, sR1_Rsq, sR2_MR, sR2_Rsq, sR3_MR, sR3_Rsq, sR4_MR, sR4_Rsq]

pdf1_qcd = [mr0_1,mr0_1s, r0_1, r0_1s, b_1, b_1s]# n_1, n_1s]
#pdf2_qcd = [mr0_2,mr0_2s, r0_2, r0_2s, b_2, b_2s]
other_par = [lumi, ntot]

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


fout.write("others_QCD = [")

for ii in range(len(other_par)):
    if ii != len(other_par) - 1:
        fout.write("'" + other_par[ii] + "',")
    else:
        fout.write("'" + other_par[ii] + "']\n")
