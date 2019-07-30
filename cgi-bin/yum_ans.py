#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type:text/html\n")

launch = sp.getstatusoutput(f"""sudo ansible-playbook yum.yml""")
if launch[0] == 0:
        print("<h3>Yum Successfully configured</h3>")
else:
        print("<h3>Unable to configure yum</h3>")

