#!/usr/bin/python36

import subprocess as sp
import cgi
import os 

print("content-type:text/html\n")

data = cgi.FieldStorage()
to = data.getvalue('to')
msg = data.getvalue('msg')

launch = os.system(f'sudo ansible-playbook --extra-vars "to={to} message={msg}" message.yml')
print(launch)
if launch == 0:
	print("Message sent")
else:
	print("Failed to send the message")
