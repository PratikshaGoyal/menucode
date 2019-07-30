#!/usr/bin/python36

import subprocess as sp
import cgi,cgitb
cgitb.enable()

print("content-type:text/html\n")

data = cgi.FieldStorage()
access_key = data.getvalue('access')
secret_key = data.getvalue('secret')

launch = sp.getstatusoutput(f"""sudo ansible-playbook aws_ec2.yml --extra-vars 'access_key={access_key} secret_key={secret_key}'""")
if launch[0] == 0:
        print("<h3>EC2 Instance Launched</h3>")
else:
        print("<h3>Unable to launch EC2 instance</h3>")
