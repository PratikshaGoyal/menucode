#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type:text/html\n")

launch = sp.getstatusoutput(f"""sudo ansible-playbook httpd.yml""")
if launch[0] == 0:
        print("<h3>Web Server Successfully configured</h3>")
else:
        print("<h3>Unable to configure web server</h3>")

