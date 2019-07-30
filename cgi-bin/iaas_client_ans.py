#!/usr/bin/python36

import subprocess as sp
import cgi
import os

print("content-type:text/html\n")

data = cgi.FieldStorage()
server_ip = data.getvalue('ip')

os.system("sudo ansible-playbook iaas_client.yml --extra-vars 'ip={server_ip}'")



