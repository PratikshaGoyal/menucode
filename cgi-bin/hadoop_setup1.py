#!/usr/bin/python36

import cgi

print("content-type:text/html\n")

choice = 'YES'

def choice():

	print("Enter ip :") 
	print("<input type='text' name='ipa'><br>")
	print("Enter password :")
	print("<input type='password' name='pass'><br>")
	print("Do you want to enter more hosts ?")
	print("<input type='submit' value='YES' name='choice'> <input type='submit' value='NO' name='choice'> <br>")
	print("<input type='submit'>")

	
print("<form action='http://192.168.43.115/cgi-bin/hadoop_setup.py'/>")
#print("</form>")

if choice == 'YES':
	choice()
	input_data= cgi.FieldStorage()
	choice = input_data.getvalue('choice')
	print(choice)
		

