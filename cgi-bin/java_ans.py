#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type:text/html\n")

launch = sp.getstatusoutput(f"""sudo ansible-playbook java.yml""")
if launch[0] == 0:
        print("<h3>Java Successfully installed</h3>")
else:
        print("<h3>Unable to install java </h3>")

