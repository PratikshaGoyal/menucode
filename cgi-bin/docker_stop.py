#!/usr/bin/python36

import subprocess
import cgi

print("content-type: text/html")

form=cgi.FieldStorage()
cname=form.getvalue("s")
cmd= "sudo docker stop {}".format(cname)
x=subprocess.getoutput(cmd)
print("location: http://192.168.43.115/cgi-bin/docker_run.py")
print()

