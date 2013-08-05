import ROOT as rt
import os,sys

list = open(sys.argv[1],"r")
lines = list.readlines()

hist = rt.TH2D("h","GMSB Gluino_XX_Squark_YY_375 Efficiency",8,1200,2000,8,1220,2020)

for ii in lines:
    print ii
    file = rt.TFile(ii.rstrip("\n"))
    m1 = int(ii.split("/")[-1].split("_")[1])
    m2 = int(ii.split("/")[-1].split("_")[2])
    npass = file.Get("HggOutput").GetEntries("PFMR>0")

    hist.Fill(m1,m2,npass/10000.)

hist.GetXaxis().SetTitle("m_{#tilde{g}} [GeV]")
hist.GetYaxis().SetTitle("m_{#tilde{q}} [GeV]")

hist.GetXaxis().SetTitleSize(.07)
hist.GetYaxis().SetTitleSize(.07)
hist.GetXaxis().SetLabelSize(.05)
hist.GetYaxis().SetLabelSize(.05)
hist.SaveAs("signal_eff.root")
