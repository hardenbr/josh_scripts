import os
import ROOT as rt
import math
import sys

input_file = sys.argv[1]

file = rt.TFile(input_file,"READ")
result = file.Get("Had/independentFR")
pars = result.floatParsFinal()

pars.Print()

text_output = "\\begin{document}\n"
text_output += "\\begin{table}[!ht]\n"
text_output += "\\begin{center}\n"
text_output += "\\begin{tabular}{|c|c|c|}\n"
text_output += "\hline \n"
text_output += "Parameter & Component 1 & Component 2\\\\ \n"
text_output += "\hline \n"
text_output += " $M_R^0$ & %3.2f $\pm$ %3.2f & %3.2f $\pm$ %3.2f \\\\ \n" % (pars[0].getVal(), pars[0].getError(), pars[1].getVal(), pars[1].getError())
text_output += "\hline \n"
text_output += " $R^2_0$ & %3.3f $\pm$ %3.3f & %3.3f $\pm$ %3.3f\\\\ \n"% (pars[3].getVal(),pars[3].getError(),pars[4].getVal(),pars[4].getError())
text_output += "\hline \n"
text_output += " $b$ & %3.2f $\pm$ %3.2f & %3.2f $\pm$ %3.2f\\\\ \n" % (pars[5].getVal(),pars[5].getError(),pars[6].getVal(),pars[6].getError())
text_output += "\hline \n"
text_output += " $n$ & %3.2f $\pm$ %3.2f & %3.2f $\pm$ %3.2f\\\\ \n" % (1.0,0,pars[8].getVal(),pars[8].getError())
text_output += "\hline \n"
text_output += " norm & %5.0f $\pm$ %5.0f &%5.0f $\pm$ %5.0f\\\\ \n" % ( pars[2].getVal()*(1 - pars[7].getVal()), pars[2].getVal()*(pars[7].getError()),  pars[2].getVal()*(pars[7].getVal()), pars[2].getVal()*(pars[7].getError()))
text_output += "\hline \n"
text_output += "\end{tabular}\n"
text_output += "\end{center}\n"
text_output += "\end{table}\n"

print text_output

