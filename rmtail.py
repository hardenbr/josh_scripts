import os,sys

if (len(sys.argv) != 2) and (len(sys.argv) != 4):
    print "usage: rmtail nremove"
    print "optional usage: rmhead <nremove> <sorting_separator> <separator_position>"

nremove = sys.argv[1]
if len(sys.argv)==4:
    tab = sys.argv[2]
    pos = sys.argv[3]
    cmd = "ls -GFhtrl | sort -t%s -nk %s | grep $USER | tail -n%s | awk '{print \"rm \" $8}'" % (tab,pos,nremove)
    print cmd,
if len(sys.argv)==2:
    cmd = "ls -GFhtrl | grep $USER | tail -n%s | awk '{print \"rm \" $8}'" % nremove
    print cmd,
