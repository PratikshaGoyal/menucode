#!/usr/bin/python36

import subprocess 

print("content-type: text/html")
print()


cmd = "sudo docker ps -a"

output = subprocess.getoutput(cmd)
container_list= output.split("\n")
print("<a href='http://192.168.43.115/cgi-bin/d.py' target='box1'>start a new docker</a>")
print("<br><br>")

print("""
<table border='5' width='100%'>
<tr>
<th>Container Name</th>
<th>Image Name</th>
<th>Status</th>
<th>Start</th>
<th>Stop</th>
<th>Terminate</th>
<th>Console</th>
</tr>""")
for c in container_list[1:]:
	if "Up" in c:
	      cstatus= "running"
	elif "Exited" in c:
	      cstatus= "Stopped"
	else:
	      cstatus= "unknown status"
	c_details = c.split()
	cname=c_details[-1]
	imagename=c_details[1]
	print('''
		
        <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td><a href='http://192.168.43.115/cgi-bin/docker_start.py?s={}'>Start</a></td>
        <td><a href='http://192.168.43.115/cgi-bin/docker_stop.py?s={}'>Stop</a></td>
        <td><a href='http://192.168.43.115/cgi-bin/docker_terminate.py?s={}'>Terminate</a></td>
        <td><a target='myconsole' a href= 'http://192.168.43.115:4200'>Console</a></td>
        </tr>
	
        '''.format( cname,imagename,cstatus,cname,cname,cname ))
print("</table>")

print("<br><br><a href=http://192.168.43.115/cgi-bin/docker_run.py>Reload</a>")	
