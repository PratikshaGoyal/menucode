#!/usr/bin/python36

import subprocess as sp
import cgi,cgitb
cgitb.enable()

print("content-type:text/html\n")

data = cgi.FieldStorage()
mail_id = data.getvalue('id')
password = data.getvalue('pass')
recipients = data.getvalue('rec')
subject = data.getvalue('sub')
body = data.getvalue('body')

launch = sp.getstatusoutput(f"""sudo ansible-playbook mail.yml --extra-vars 'mail_id={mail_id} password={password} recipients={recipients} subject={subject} body={body}'""")
if launch[0] == 0:
	print("<h3>Mail Sent</h3>")
else:
	print("<h3>Unable to send mail</h3>")
