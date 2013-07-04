{
  gROOT->SetStyle("Plain"); // remove gray background from plots
  //gSystem->Load("libMinuit.so") ;
  //gSystem->Load("$ROOTSYS/lib/libRooFitCore.so") ;
  //gSystem->Load("$ROOTSYS/lib/libRooFitModels.so") ;
  gStyle->SetPalette(1);
 gStyle->SetTitleFontSize(.05);
  gStyle->SetLabelSize(.049,"xy");
  gStyle->SetTitleXSize(.045);
  gStyle->SetTitleYSize(.045);

  TCanvas c1;

  outTreeGG->Draw("PFR^2:PFMR>>hist","PFMR>150 && PFR^2>.03","colz");
  gStyle->SetOptStat(0);
  hist.GetXaxis().SetTitle("M_{R} [GeV]");
  hist.GetYaxis().SetTitle("R^{2}");
  
  hist.SetTitle("M_{R} vs. R^{2} Tight-Tight Sample");
  
  hist.Draw("colz");

  c1.SaveAs("mr_rsq_tt.pdf");
  c1.SaveAs("mr_rsq_tt.C");

  gStyle->SetOptStat(0);
  outTreeFF->Draw("PFR^2:PFMR>>hist2","PFMR>150 && PFR^2>.03","colz");
  gStyle->SetOptStat(0);
  hist2.GetXaxis().SetTitle("M_{R} [GeV}");
  hist2.GetYaxis().SetTitle("R^{2}");
  
  hist2.SetTitle("M_{R} vs. R^{2} Control Sample");

  hist2.Draw("colz");

  c1.SaveAs("mr_rsq_ff.pdf");
  c1.SaveAs("mr_rsq_ff.C");

}
