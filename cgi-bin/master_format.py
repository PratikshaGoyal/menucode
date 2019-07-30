#!/usr/bin/python36	

import os 
import subprocess as sp
import cgi

print("content-type: text/html\n")
data = cgi.FieldStorage()
x = sp.getstatusoutput('sudo ansible namenode -m command -a "hadoop namenode -format"')
print(x)
