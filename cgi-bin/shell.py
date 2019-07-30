#!/usr/bin/python36
import os
import subprocess as sp
import cgi

print("content-type: text/html")
print()

data = cgi.FieldStorage()
ip = data.getvalue('ip')
print(f"<br/><a href='http://{ip}:4200' target='myCAAS'>get shell in a box</a><br/><br/><br/>")
print("<iframe width='300px' height='300px' name='myCAAS'></iframe>")
