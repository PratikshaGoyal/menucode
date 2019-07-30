#!/usr/bin/python36

import subprocess as sp

print("content-type: text/html")
print()

#x=sp.getoutput("sudo docker run -d -i -t --name {} {} ".format)
#print(x)


print("<form action='docker_ans.py'>")
print("enter docker name :")
print("<input name='name'>")

print("<br />")
print("enter docker image :")
print("<input name='img'>")
print("</ select>")
print("<input type ='submit'value='Launch Docker' />")
print("<br><a href='http://192.168.43.115/cgi-bin/docker_run.py' target='box'>Back</a>")
print("</form>")
