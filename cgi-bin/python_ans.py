#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type:text/html\n")

launch = sp.getstatusoutput(f"""sudo ansible-playbook python.yml""")
if launch[0] == 0:
        print("<h3>Python Successfully installed</h3>")
else:
        print("<h3>Unable to install python </h3>")

