import os
print "bjobs | awk '{print \"bkill \" $1}'"
os.system(" bjobs | grep -v JOBID | awk '{print \"bkill \" $1}'|bash")
