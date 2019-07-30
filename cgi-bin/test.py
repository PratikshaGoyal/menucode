#!/usr/bin/python36

import subprocess

print("content-type: text/html")
print()


cmd = "sudo docker ps -a"

output = subprocess.getoutput(cmd)
container_list= output.split("\n")
print(container_list)
