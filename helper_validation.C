#include <vector> 
void helper_validation(){
  Int_t font = 42;

  gStyle->SetPalette(1);
  gStyle->SetTitleX(0.3);
  gStyle->SetTitleW(0.4);
  gStyle->SetCanvasBorderMode(0);
  gStyle->SetCanvasColor(kWhite);
  gStyle->SetCanvasDefH(600); //Height of canvas
  gStyle->SetCanvasDefW(800); //Width of canvas
  gStyle->SetCanvasDefX(0);   //POsition on screen
  gStyle->SetCanvasDefY(0);

  gStyle->SetPadBorderMode(0);
  // gStyle->SetPadBorderSize(Width_t size = 1);
  gStyle->SetPadColor(kWhite);
  gStyle->SetPadGridX(false);
  gStyle->SetPadGridY(false);
  gStyle->SetGridColor(0);
  gStyle->SetGridStyle(3);
  gStyle->SetGridWidth(1);

  //for the frame
  gStyle->SetFrameBorderMode(0);
  gStyle->SetFrameBorderSize(1);
  gStyle->SetFrameFillColor(0);
  gStyle->SetFrameFillStyle(0);
  gStyle->SetFrameLineColor(1);
  gStyle->SetFrameLineStyle(1);
  gStyle->SetFrameLineWidth(1);

  gStyle->SetPaperSize(20,26);
  gStyle->SetPadTopMargin(0.1);
  gStyle->SetPadRightMargin(0.12);
  gStyle->SetPadBottomMargin(0.2);
  gStyle->SetPadLeftMargin(0.17);

  gStyle->SetTitleBorderSize(0);
  gStyle->SetTitleFont(font,"xyz");  // set the all 3 axes title font
  gStyle->SetTitleFont(font," ");    // set the pad title font
  gStyle->SetTitleSize(0.06,"xyz"); // set the 3 axes title size
  gStyle->SetTitleSize(0.06," ");   // set the pad title size
  gStyle->SetTitleFillColor(0);
  gStyle->SetLabelFont(font,"xyz");
  gStyle->SetLabelSize(0.035,"xyz");
  gStyle->SetLabelColor(1,"xyz");
  gStyle->SetTextFont(font);
  gStyle->SetTextSize(0.08);
  gStyle->SetStatFont(font);

  //tick marks
  gStyle->SetPadTickX(1);
  gStyle->SetPadTickY(1);

  const Int_t NRGBs = 5;
  const Int_t NCont = 255;
  Double_t stops[NRGBs] = { 0.00, 0.34, 0.61, 0.84, 1.00 };
  Double_t red[NRGBs] = { 0.00, 0.00, 0.87, 1.00, 0.51 };
  Double_t green[NRGBs] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
  Double_t blue[NRGBs] = { 0.51, 1.00, 0.12, 0.00, 0.00 };
  TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
  gStyle->SetNumberContours(NCont);


  vector<TString> var_names;
  vector<TString> var_titles;

  vector<TString> razor_var_names;
  vector<TString> razor_var_titles;

  vector<TString> razor_var_names_SS;
  vector<TString> razor_var_titles_SS;

  vector<TString> razor_var_names_OS;
  vector<TString> razor_var_titles_OS;

  vector<float> min_x;
  vector<float> max_x;

  vector<float> razor_min_x;
  vector<float> razor_max_x;

  vector<float> razor_min_x_SS;
  vector<float> razor_max_x_SS;

  vector<float> razor_min_x_OS;
  vector<float> razor_max_x_OS;

  vector<bool> isLog;
  vector<bool> razor_isLog;

  TCut baseline  = "PFMR > 0 && PFR^2 > 0" ;
  int n_bins = 40;  

  //add the variable names
  var_names.push_back("nJets");
  min_x.push_back(0.);
  max_x.push_back(10.);
  var_titles.push_back("Number of Jets");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.isosumBad[0]");
  min_x.push_back(-4.);
  max_x.push_back(15.);
  var_titles.push_back("Sub Leading Photon Bad Isolation Sum [GeV]");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.isosumBad[1]");
  min_x.push_back(-4.);
  max_x.push_back(15.);
  var_titles.push_back("Leading Photon Bad Isolation Sum [GeV]");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.isosumGood[0]");
  min_x.push_back(-1.);
  max_x.push_back(7.);
  var_titles.push_back("Sub Leading Photon Good Isolation Sum [GeV]");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.isosumGood[1]");
  min_x.push_back(-1);
  max_x.push_back(7.);
  var_titles.push_back("Leading Photon Good Isolation Sum [GeV]");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.pt[0]");
  min_x.push_back(0.);
  max_x.push_back(300.);
  var_titles.push_back("Sub Leading Photon P_{t}");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.pt[0]");
  min_x.push_back(0.);
  max_x.push_back(300.);
  var_titles.push_back("Sub Leading Photon P_{t}");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.pt[1]");
  min_x.push_back(0);
  max_x.push_back(300);
  var_titles.push_back("Leading Photon P_{t}");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.eta[0]");
  min_x.push_back(-3);
  max_x.push_back(3);
  var_titles.push_back("Sub Leading Photon #eta");
  isLog.push_back(false);

  var_names.push_back("PhotonPFCiC.eta[1]");
  min_x.push_back(-3);
  max_x.push_back(3);
  var_titles.push_back("Leading Photon #eta");
  isLog.push_back(false);

  var_names.push_back("PhotonPFCiC.phi[0]");
  min_x.push_back(-3.15);
  max_x.push_back(3.15);
  var_titles.push_back("Sub Leading Photon #phi");
  isLog.push_back(false);

  var_names.push_back("PhotonPFCiC.phi[1]");
  min_x.push_back(-3.15);
  max_x.push_back(3.15);
  var_titles.push_back("Leading Photon #phi");
  isLog.push_back(false);

  var_names.push_back("PhotonPFCiC.sieie[0]");
  min_x.push_back(0);
  max_x.push_back(.015);
  var_titles.push_back("Sub Leading Photon #sigma_{i#eta i#eta}");
  isLog.push_back(false);

  var_names.push_back("PhotonPFCiC.sieie[1]");
  min_x.push_back(0);
  max_x.push_back(.015);
  var_titles.push_back("Leading Photon #sigma_{ i#eta i#eta}");
  isLog.push_back(false);

  var_names.push_back("PhotonPFCiC.r9[0]");
  min_x.push_back(0);
  max_x.push_back(1.2);
  var_titles.push_back("Sub Leading Photon r_{9}");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.r9[1]");
  min_x.push_back(0);
  max_x.push_back(1.2);
  var_titles.push_back("Leading Photon r_{9}");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.HoverE[0]");
  min_x.push_back(0);
  max_x.push_back(.1);
  var_titles.push_back("Sub Leading Photon H/E");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.HoverE[1]");
  min_x.push_back(0);
  max_x.push_back(.1);
  var_titles.push_back("Leading Photon H/E");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.dr03EcalIso[0]");
  min_x.push_back(-2);
  max_x.push_back(10);
  var_titles.push_back("Sub Leading Photon Ecal Iso #Delta R=.03");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.dr03EcalIso[1]");
  min_x.push_back(-2);
  max_x.push_back(10);
  var_titles.push_back("Leading Photon Ecal Iso #Delta R=.03");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.dr04HcalIso[0]");
  min_x.push_back(-2);
  max_x.push_back(13);
  var_titles.push_back("Sub Leading Photon Hcal Iso #Delta R=.04");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.dr04HcalIso[1]");
  min_x.push_back(-2);
  max_x.push_back(13);
  var_titles.push_back("Leading Photon Hcal Iso #Delta R=.04");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.dr03TrackIso[0]");
  min_x.push_back(-1);
  max_x.push_back(1);
  var_titles.push_back("Sub Leading Photon Track Iso #Delta R=.03");
  isLog.push_back(true);

  var_names.push_back("PhotonPFCiC.dr03TrackIso[1]");
  min_x.push_back(-1);
  max_x.push_back(1);
  var_titles.push_back("Leading Photon Track Iso #Delta R=.03");
  isLog.push_back(true);

  var_names.push_back("MET");
  min_x.push_back(0);
  max_x.push_back(100);
  var_titles.push_back("MET");
  isLog.push_back(false);

  var_names.push_back("METPhi");
  min_x.push_back(-4);
  max_x.push_back(4);
  var_titles.push_back("#phi_{MET}");
  isLog.push_back(false);

  var_names.push_back("mPairPFCiC");
  min_x.push_back(0);
  max_x.push_back(600);
  var_titles.push_back("m_{#gamma#gamma}");
  isLog.push_back(false);

  // USUAL RAZOR VARIABLES
  razor_var_names.push_back("PFMR");
  razor_min_x.push_back(0);
  razor_max_x.push_back(2000);
  razor_var_titles.push_back("M_{R} [GeV]");
  razor_isLog.push_back(true);

  razor_var_names.push_back("PFR^2");
  razor_min_x.push_back(0);
  razor_max_x.push_back(1.2);
  razor_var_titles.push_back("R^{2} [GeV]");
  razor_isLog.push_back(true);

  razor_var_names.push_back("ptHem1");
  razor_min_x.push_back(0);
  razor_max_x.push_back(300);
  razor_var_titles.push_back("p_{t} Hemisphere 1  [GeV]");
  razor_isLog.push_back(false);

  razor_var_names.push_back("ptHem2");
  razor_min_x.push_back(0);
  razor_max_x.push_back(300);
  razor_var_titles.push_back("p_{t} Hemisphere 2 [GeV]");
  razor_isLog.push_back(false);

  razor_var_names.push_back("etaHem1");
  razor_min_x.push_back(-5);
  razor_max_x.push_back(5);
  razor_var_titles.push_back("#eta Hemisphere 1");
  razor_isLog.push_back(false);

  razor_var_names.push_back("etaHem2");
  razor_min_x.push_back(-5);
  razor_max_x.push_back(5);
  razor_var_titles.push_back("#eta Hemisphere 2");
  razor_isLog.push_back(false);

  razor_var_names.push_back("phiHem1");
  razor_min_x.push_back(-3.2);
  razor_max_x.push_back(3.2);
  razor_var_titles.push_back("#phi Hemisphere 1");
  razor_isLog.push_back(false);

  razor_var_names.push_back("phiHem2");
  razor_min_x.push_back(-3.2);
  razor_max_x.push_back(3.2);
  razor_var_titles.push_back("#phi Hemisphere 2");
  razor_isLog.push_back(false);

  razor_var_names.push_back("mHem1");
  razor_min_x.push_back(0);
  razor_max_x.push_back(400);
  razor_var_titles.push_back("M_{Hemisphere 1} [GeV]");
  razor_isLog.push_back(false);

  razor_var_names.push_back("mHem2");
  razor_min_x.push_back(0);
  razor_max_x.push_back(400);
  razor_var_titles.push_back("M_{Hemipshere 2} [GeV]");
  razor_isLog.push_back(false);

  // SS RAZOR VARIABLES
  razor_var_names_SS.push_back("PFMR_SS");
  razor_var_titles_SS.push_back("M_{R} SS [GeV]");

  razor_var_names_SS.push_back("PFR_SS^2");
  razor_var_titles_SS.push_back("R^{2} SS ");

  razor_var_names_SS.push_back("ptHem1_SS");
  razor_var_titles_SS.push_back("p_{t} Hemisphere 1 SS (#gamma#gamma) [GeV]");

  razor_var_names_SS.push_back("ptHem2_SS");
  razor_var_titles_SS.push_back("p_{t} Hemisphere 2 SS [GeV]");

  razor_var_names_SS.push_back("etaHem1_SS");
  razor_var_titles_SS.push_back("#eta Hemisphere 1 SS (#gamma#gamma)");

  razor_var_names_SS.push_back("etaHem2_SS");
  razor_var_titles_SS.push_back("#eta Hemisphere 2 SS");

  razor_var_names_SS.push_back("phiHem1_SS");
  razor_var_titles_SS.push_back("#phi Hemisphere 1 SS (#gamma#gamma)");

  razor_var_names_SS.push_back("phiHem2_SS");
  razor_var_titles_SS.push_back("#phi Hemisphere 2 SS ");

  razor_var_names_SS.push_back("mHem1_SS");
  razor_var_titles_SS.push_back("M_{Hem1} SS (#gamma#gamma) [GeV]");

  razor_var_names_SS.push_back("mHem2_SS");
  razor_var_titles_SS.push_back("M_{Hem2} SS [GeV]");

  //OS Variables
  // SS RAZOR VARIABLES
  razor_var_names_OS.push_back("PFMR_OS");
  razor_var_titles_OS.push_back("M_{R} OS [GeV]");

  razor_var_names_OS.push_back("PFR_OS^2");
  razor_var_titles_OS.push_back("R^{2} OS");

  razor_var_names_OS.push_back("ptHem1_OS");
  razor_var_titles_OS.push_back("p_{t} Hemisphere 1 OS [GeV]");

  razor_var_names_OS.push_back("ptHem2_OS");
  razor_var_titles_OS.push_back("p_{t} Hemisphere 2 OS [GeV]");

  razor_var_names_OS.push_back("etaHem1_OS");
  razor_var_titles_OS.push_back("#eta Hemisphere 1 OS ");

  razor_var_names_OS.push_back("etaHem2_OS");
  razor_var_titles_OS.push_back("#eta Hemisphere 2 OS");

  razor_var_names_OS.push_back("phiHem1_OS");
  razor_var_titles_OS.push_back("#phi Hemisphere 1 OS ");

  razor_var_names_OS.push_back("phiHem2_OS");
  razor_var_titles_OS.push_back("#phi Hemisphere 2 OS");

  razor_var_names_OS.push_back("mHem1_OS");
  razor_var_titles_OS.push_back("M_{Hem1} OS [GeV]");

  razor_var_names_OS.push_back("mHem2_OS");
  razor_var_titles_OS.push_back("M_{Hem2} OS [GeV]");



    //canvas and histogram
  TCanvas c1;
  TH1F * temp_hist;
  //  TPaveText *pt = new TPaveText(.5,.53,.5,.5,"NDC");
  TPaveText *pt = new TPaveText();
  pt->AddText("CMS Preliminary #sqrt{s} = 8 TeV");
  pt->AddText("Run 2012D DoublePhoton");
  pt->AddText("#int L dt ~7 fb^{-1}");
  pt->SetFillColor(kWhite);

  //do the typical variables
  for(int ii = 0; ii < var_names.size(); ii++) {
    if (ii == 0) n_bins = 10; //jets are binned differently
    else n_bins = 40;

    //build the hist name
    TString hist_name = Form("hist_%i", ii);

    //make the histogram
    temp_hist = new TH1F(hist_name,hist_name,n_bins,min_x[ii],max_x[ii]);
    //make the draw command
    TString draw_cmd= var_names[ii].Append(Form(">>hist_%i",ii));
                   
    cout << draw_cmd << endl;
    HggOutput->Draw(draw_cmd,baseline);

    temp_hist->Draw();
    pt->Draw("same")
    //set the axis and style
    gStyle->SetOptStat(1111);
    //    temp_hist.GetXaxis().SetTitle();
    //    temp_hist.GetXaxis().SetRange(min_x[ii],max_x[ii]);
    temp_hist.GetXaxis().SetTitle(var_titles[ii]);
    temp_hist.GetYaxis().SetTitle("N Events");
    
    temp_hist.SetTitle("");
    //    temp_hist.SetMinimum(min_events);
    //    temp_hist.SetMaximum(max_events);
    TString c_save = hist_name;
    TString pdf_save = hist_name;
    
    if( isLog[ii]) c1.SetLogy(1);
    else c1.SetLogy(0);

    c_save.Append(".C");
    pdf_save.Append(".pdf");

    c1.SaveAs(c_save);
    c1.SaveAs(pdf_save);
  }

  //do the razor variables
  for(int ii = 0; ii < razor_var_names.size(); ii++) {

    //build the hist name
    TString hist_name = Form("rhist_%i", ii);
    //make the histogram
    temp_hist = new TH1F(hist_name,hist_name,n_bins,razor_min_x[ii],razor_max_x[ii]);
    //make the draw command
    TString draw_cmd= razor_var_names[ii].Append(Form(">>rhist_%i",ii));                  
    cout << draw_cmd << endl;
    
    //draw the variable into the histogram
    HggOutput->Draw(draw_cmd,baseline);
    temp_hist->Draw();
    pt->Draw("same")
    //set the axis and style
    gStyle->SetOptStat(1111);
    //    temp_hist.GetXaxis().SetTitle();
    //    temp_hist.GetXaxis().SetRange(min_x[ii],max_x[ii]);
    temp_hist.GetXaxis().SetTitle(razor_var_titles[ii]);
    temp_hist.GetYaxis().SetTitle("N Events");
    
    temp_hist.SetTitle("");

    if( razor_isLog[ii]) c1.SetLogy(1);
    else c1.SetLogy(0);

    //    temp_hist.SetMinimum(min_events);
    //    temp_hist.SetMaximum(max_events);
    TString c_save = hist_name;
    TString pdf_save = hist_name;    
    c_save.Append(".C");
    pdf_save.Append(".pdf");

    c1.SaveAs(c_save);
    c1.SaveAs(pdf_save);
  }

  //SS VARIABLE DRAWING
  //do the razor variables
  for(int ii = 0; ii < razor_var_names_SS.size(); ii++) {
    //build the hist name
    TString hist_name = Form("rhist_ss_%i", ii);
    //make the histogram
    temp_hist = new TH1F(hist_name,hist_name,n_bins,razor_min_x[ii],razor_max_x[ii]);
    //make the draw command
    TString draw_cmd= razor_var_names_SS[ii].Append(Form(">>rhist_ss_%i",ii));                  
    cout << draw_cmd << endl;
    
    //draw the variable into the histogram
    HggOutput->Draw(draw_cmd,baseline);
    temp_hist->Draw();
    pt->Draw("same")
    //set the axis and style
    gStyle->SetOptStat(1111);
    //    temp_hist.GetXaxis().SetTitle();
    //    temp_hist.GetXaxis().SetRange(min_x[ii],max_x[ii]);
    temp_hist.GetXaxis().SetTitle(razor_var_titles_SS[ii]);
    temp_hist.GetYaxis().SetTitle("N Events");
    
    temp_hist.SetTitle("");
    //    temp_hist.SetMinimum(min_events);
    //    temp_hist.SetMaximum(max_events);
    TString c_save = hist_name;
    TString pdf_save = hist_name;

    if( razor_isLog[ii]) c1.SetLogy(1);
    else c1.SetLogy(0);
    
    c_save.Append(".C");
    pdf_save.Append(".pdf");

    c1.SaveAs(c_save);
    c1.SaveAs(pdf_save);
  }

  //OS RAZOR VARIABLES
  for( int ii = 0; ii < razor_var_names_OS.size(); ii++) {
    //build the hist name
    TString hist_name = Form("rhist_os_%i", ii);
    //make the histogram
    temp_hist = new TH1F(hist_name,hist_name,n_bins,razor_min_x[ii],razor_max_x[ii]);
    //make the draw command
    TString draw_cmd= razor_var_names_OS[ii].Append(Form(">>rhist_os_%i",ii));                  
    cout << draw_cmd << endl;
    
    //draw the variable into the histogram
    HggOutput->Draw(draw_cmd,baseline);
    temp_hist->Draw();

    //set the axis and style
    gStyle->SetOptStat(1111);
    //    temp_hist.GetXaxis().SetTitle();
    //    temp_hist.GetXaxis().SetRange(min_x[ii],max_x[ii]);
    temp_hist.GetXaxis().SetTitle(razor_var_titles_OS[ii]);
    temp_hist.GetYaxis().SetTitle("N Events");
    
    temp_hist.SetTitle("");

    if( razor_isLog[ii]) c1.SetLogy(1);
    else c1.SetLogy(0);

    pt->Draw("same")
    //    temp_hist.SetMinimum(min_events);
    //    temp_hist.SetMaximum(max_events);
    TString c_save = hist_name;
    TString pdf_save = hist_name;
    
    c_save.Append(".C");
    pdf_save.Append(".pdf");

    c1.SaveAs(c_save);
    c1.SaveAs(pdf_save);
  }
}
