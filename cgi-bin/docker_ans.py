#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type:text/html\n")

data = cgi.FieldStorage()
name = data.getvalue('name')
img = data.getvalue('img')
launch = sp.getstatusoutput(f"sudo ansible-playbook docker.yml --extra-vars 'name_os={name} image={img}'")
print(launch)
if launch[0] == 0:
	print("<h3>Successfully Launched</h3>")
else:
	print("<h3>Unable to launch docker</h3>")
