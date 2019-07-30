#!/usr/bin/python36

import subprocess as sp
import cgi
import os

print("content-type:text/html\n")

data = cgi.FieldStorage()
server_ip = data.getvalue('ip')

os.system("sudo ansible-playbook iaas_web.yml")
launch = os.system("sudo novnc_server  --vnc  {server_ip}:5905")
print(launch)

