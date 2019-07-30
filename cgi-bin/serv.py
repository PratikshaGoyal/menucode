#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()
mydata=cgi.FieldStorage()
y=mydata.getvalue('n')
x=sp.getstatusoutput("sudo ansible-playbook serv.yml --extra-vars 'x={}'".format(y))
if(x[0]==0):
        print("<h1> Service Started</h1>")
else:
        print("<h1> Unsucessfull</h1>")

