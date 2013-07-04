{
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


  vector<string> var_names;
  vector<string> var_titles;

  vector<string> razor_var_SS;
  vector<string> razor_var_SS_titles;

  vector<string> razor_var_OS;
  vector<string> razor_var_OS_titles;

  vector<float> min_x;
  vector<float> max_x;

  TCut baseline  = "PFMR > 0 && PFR^2 > 0" 
  vector<int> n_bins;

  //add the variable names
  var_names.push_back("PhotonPFCiC.pt[0]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.pt[1]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.eta[0]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.eta[1]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.phi[0]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.phi[1]");
  var_titles.push_back("");

  var_names.push_back("PhotonPFCiC.sieie[0]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.sieie[1]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.r9[0]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.r9[1]");

  var_names.push_back("PhotonPFCiC.HoverE[0]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.HoverE[1]");
  var_titles.push_back("");

  var_names.push_back("PhotonPFCiC.dr03EcalIso[0]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.dr03EcalIso[1]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.dr04HcalIso[0]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.dr04HcalIso[1]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.dr03TrackIso[0]");
  var_titles.push_back("");
  var_names.push_back("PhotonPFCiC.dr03Trackso[1]");
  var_titles.push_back("");
  var_names.push_back("MET");
  var_titles.push_back("");
  var_names.push_back("METPhi");
  var_titles.push_back("");
  var_names.push_back("mPairPFCiC");
      
  razor_var_names.push_back("PFMR")
  razor_var_titles.push_back("");
  razor_var_names.push_back("PFR^2")
  razor_var_titles.push_back("");
  razor_var_names.push_back("ptHem1")
  razor_var_titles.push_back("");
  razor_var_names.push_back("ptHem2")
  razor_var_titles.push_back("");
  razor_var_names.push_back("etaHem1")
  razor_var_titles.push_back("");
  razor_var_names.push_back("etaHem2")
  razor_var_titles.push_back("");
  razor_var_names.push_back("phiHem1")
  razor_var_titles.push_back("");
  razor_var_names.push_back("phiHem2")
  razor_var_titles.push_back("");
  razor_var_names.push_back("mHem1")
  razor_var_titles.push_back("");
  razor_var_names.push_back("mHem2")
  razor_var_titles.push_back("");
  razor_var_names_SS.push_back("PFMR_SS")
  razor_var_names_SS.push_back("PFR_SS^2")
  razor_var_names_SS.push_back("ptHem1_SS")
  razor_var_names_SS.push_back("ptHem2_SS")
  razor_var_names_SS.push_back("etaHem1_SS")
  razor_var_names_SS.push_back("etaHem2_SS")
  razor_var_names_SS.push_back("phiHem1_SS")
  razor_var_names_SS.push_back("phiHem2_SS")
  razor_var_names_SS.push_back("mHem1_SS")
  razor_var_names_SS.push_back("mHem2_SS")

  razor_var_names_OS.push_back("PFMR_OS")
  razor_var_names_OS.push_back("PFR_OS^2")
  razor_var_names_OS.push_back("ptHem1_OS")
  razor_var_names_OS.push_back("ptHem2_OS")
  razor_var_names_OS.push_back("etaHem1_OS")
  razor_var_names_OS.push_back("etaHem2_OS")
  razor_var_names_OS.push_back("phiHem1_OS")
  razor_var_names_OS.push_back("phiHem2_OS")
  razor_var_names_OS.push_back("mHem1_OS")
  razor_var_names_OS.push_back("mHem2_OS")

  
  TH1F * hist3 = new TH1F("hist3","hist3",nbins_rsq,min_rsq,max_rsq);
  TH1F * hist4 = new TH1F("hist4","hist4",nbins_rsq,min_rsq,max_rsq);
  TH1F * hist5 = new TH1F("hist5","hist5",nbins_mr,min_mr,max_mr);
  TH1F * hist6 = new TH1F("hist6","hist6",nbins_mr,min_mr,max_mr);

  TH2F * hists_2D[2];
  TH1F * hists_1D[4];

  TCanvas c1;
  TH1F * temp_hist;


  stringstream s;
  //do the typical variables
  for(ii = 0; ii < var_names.size(); ii++) {

    //read the number
    s << ii; 
    //build the hist name
    hist_name = "hist";
    hist_name += s.str();
    s.str(""); // clear the stringstream 

    //make the histogram
    temp_hist = new TH1F(hist_name,hist_name,n_bins[ii],x_min[ii],x_max[ii]);
    //make the draw command
    var_names[ii] += ">>";
    var_names[ii] += hist_name;
    //draw it
    HggOutput->Draw(var_names[ii],baseline);

    //set the axis and style
    gStyle->SetOptStat(0);
    //    temp_hist.GetXaxis().SetTitle();
    temp_hist.GetXaxis().SetRange(x_min[ii],x_max[ii]);
    temp_hist.GetYaxis().SetTitle("N Events");
    
    temp_hist.SetTitle(var_title[ii]);
    //    temp_hist.SetMinimum(min_events);
    //    temp_hist.SetMaximum(max_events);
    
    c1.SaveAs()
  }

  //do the razor variables
  for(ii = 0; ii < razor_var_names.size(); ii++) {

  }


}
