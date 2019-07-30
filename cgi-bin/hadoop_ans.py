#!/usr/bin/python36	

import os 
import subprocess as sp
import cgi

print("content-type: text/html\n")
data = cgi.FieldStorage()

ch = data.getvalue('choice')
file_ip = data.getvalue('file')
hostname = data.getvalue('hostname')
mastername = data.getvalue('mastername')
node = data.getvalue('node')


sp.getoutput("sudo chmod 777 /etc/ansible/hosts")

sp.getoutput("sudo cp /etc/hadoop/hdfs-site.xml /var/www/cgi-bin")
sp.getoutput("sudo cp /etc/hadoop/core-site.xml /var/www/cgi-bin")
sp.getoutput("sudo cp /etc/hadoop/mapred-site.xml /var/www/cgi-bin")


#sp.getoutput("sudo chmod 666 /etc/hadoop/hdfs-site.xml")
#sp.getoutput("sudo chmod 666 /etc/hadoop/core-site.xml")
#sp.getoutput("sudo chmod 666 /etc/hadoop/mapred-site.xml")

sp.getoutput("sudo chmod 777 /var/www/cgi-bin/hdfs-site.xml")
sp.getoutput("sudo chmod 777 /var/www/cgi-bin/core-site.xml")
sp.getoutput("sudo chmod 777 /var/www/cgi-bin/mapred-site.xml")

fp = open("/etc/ansible/hosts","r")
l = fp.read()
fp.close()

fh = open("/etc/ansible/hosts","a")

if node in l:
	fh.write(f"{hostname}\tansible_user=root\tansible_ssh_pass=redhat\n")
else:
	fh.write(f"[{node}]\n")
	fh.write(f"{hostname}\tansible_user=root\tansible_ssh_pass=redhat\n")
fh.close()

def start():
	sp.getoutput(f'sudo ansible {node} -m command -a "hadoop-daemon.sh start {node}"')
	sp.getoutput('sudo ansible {node} -m command -a "iptables -F"')
	sp.getoutput('sudo ansible {node} -m command -a "jps"')


def hdfs_site(file_ip,n):
	f = open("/var/www/cgi-bin/hdfs-site.xml" ,"w")	
	f.write(f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- 	Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.{n}.dir</name>\n<value>/{file_ip}</value>\n</property>\n\n</configuration>""")
	f.close()
	
def core_site(mastername):
	f = open("/var/www/cgi-bin/core-site.xml" ,"w")	
	f.write(f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- 	Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{mastername}:9001</value>\n</property>\n\n</configuration>""")
	f.close()
	
def mapred_site(mastername):
	f = open("/var/www/cgi-bin/mapred-site.xml","w")
	f.write(f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{mastername}:9002</value>\n</property>\n\n</configuration>""")
	f.close()
	

def namenode_node_setup(file_ip,mastername,hostname):
	n="name"	
	hdfs_site(file_ip,n)
	core_site(mastername)
	x = sp.getoutput(f'sudo ansible {hostname} -m command -a "mkdir /{file_ip}"')
	y = sp.getoutput(f'sudo ansible {hostname} -m copy -a "src=/var/www/cgi-bin/hdfs-site.xml dest=/etc/hadoop/hdfs-site.xml"')
	z = sp.getoutput(f'sudo ansible {hostname} -m copy -a "src=/var/www/cgi-bin/core-site.xml dest=/etc/hadoop/core-site.xml"')
	start()
	

def datanode_node_setup(file_ip,mastername,hostname):
	n="data"	
	hdfs_site(file_ip,n)
	core_site(mastername)
	sp.getoutput(f'sudo ansible {hostname} -m command -a "mkdir /{file_ip}"')
	sp.getoutput(f'sudo ansible {hostname} -m copy -a "src=/var/www/cgi-bin/hdfs-site.xml dest=/etc/hadoop"')	
	sp.getoutput(f'sudo ansible {hostname} -m copy -a "src=/var/www/cgi-bin/core-site.xml dest=/etc/hadoop"')	
	start()


def client_node_setup(mastername,hostname):
	os.system(f"sudo mkdir {file_ip}")
	no_of_replicas = input("enter no. of replicas : ")
	f = open("/var/www/cgi-bin/hdfs-site.xml" ,"w")	
	f.write(f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- 	Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.replication</name>\n<value>{no_of_replicas}</value>\n</property>\n\n</configuration>""")
	f.close()

	core_site(mastername)
	sp.getoutput('sudo ansible {hostname} -m copy -a "src=/var/www/cgi-bin/hdfs-site.xml dest=/etc/hadoop"')	


if ch == "MasterNode":
	namenode_node_setup(file_ip,mastername,hostname)
	#report = sp.getstatusoutput("sudo hadoop dfsadmin -report")
	
	#if report[0]==0:
	#	print("<h4>node successfully configured</h4>")
	#else:
	#	print("<h3>unable to configure your node</h3>")

elif ch == "SlaveNode":
	datanode_node_setup(file_ip,mastername,hostname)

elif ch == "JobTracker":
	print("hi")
	mapred_site(hostname)
	print("bye")
	core_site(hostname)
	print("welcome")
	sp.getoutput('sudo ansible jobtracker -m copy -a "src=/var/www/cgi-bin/mapred-site.xml dest=/etc/hadoop"')	
	sp.getoutput('sudo ansible jobtracker -m copy -a "src=/var/www/cgi-bin/core-site.xml dest=/etc/hadoop"')
	start()
	print("getlost")

elif ch == "TaskTracker":
	mapred_site(hostname)
	sp.getoutput('sudo ansible tasktracker -m copy -a "src=/var/www/cgi-bin/mapred-site.xml dest=/etc/hadoop"')	
	sp.getoutput('sudo ansible tasktracker -m copy -a "src=/var/www/cgi-bin/core-site.xml dest=/etc/hadoop"')
	start()

elif ch == "Client":
	client_node_setup(mastername,hostname)

elif ch == "upload":
	filename = input("Enter the name of file you want to upload : ") 
	op = sp.getstatusoutput('sudo ansible client -m command -a "hadoop fs -put {filename} /" ')
	if op[0] == 0:
		t = "File uploded"
	else:
		t = "File not uploaded"
elif ch == "read":
	filename = input("Enter the name of file you want to read : ") 
	op = sp.getoutput('sudo ansible client -m command -a "hadoop fs -cat /{filename} " ')
	
elif ch == "delete":
	filename = input("Enter the name of file you want to remove : ") 
	op = sp.getstatusoutput('sudo ansible client -m command -a "hadoop fs -rm /{filename} " ')
	if op[0] == 0:
		t = "File Deleted"
	else:
		t = "File not deleted"
	
elif ch == "list":
	op = sp.getoutput('sudo ansible client -m command -a "hadoop fs -ls /" ')
	session.send(op.encode())
	













""" def r_node_setup():
	print(""
	press 1 : for namenode node setup
	press 2 : for datanode node setup
	press 3 : for client node setup
	press 4 : to start namenode node
	press 5 : to upload a file via cloud
	press 6 : to read a file 
	press 7 : to remove a file 

	"")
	
	x = int(input("enter your choice : "))	
	subprocess.getoutput("cp /etc/hadoop/hdfs-site.xml /var/www/cgi-bin/")
	subprocess.getoutput("cp /etc/hadoop/core-site.xml /var/www/cgi-bin/")

	if x == 1: 
		file_ip = input("enter name of file : ")
		namenode_ip=input("enter namenode's ip :")
		hostname = input("enter hostname : ")	
		r_namenode_node_setup(namenode_ip,file_ip,hostname)
		#os.system("hadoop-daemon.sh start namenode ")
		#os.system("iptables - F")
		#os.system("jps")
		#os.system("hadoop dfsadmin -report")
	elif x == 2:
		file_ip = input("enter name of file : ")
		datanode_ip=input("enter datanode's ip :")
		hostname = input("enter hostname : ")	
		r_datanode_node_setup(datanode_ip,file_ip,hostname)
		os.system("hadoop-daemon.sh start datanode ")
		os.system("iptables - F")
		os.system("jps")
	elif x == 3:
		client_ip=input("enter client's ip :")
		hostname = input("enter hostname : ")	
		r_client_node_setup(client_ip,hostname)

"""




