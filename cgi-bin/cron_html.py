#!/usr/bin/python36
import subprocess as sp
print("content-type: text/html")
print()
print('''
<form action=http://192.168.43.115/cgi-bin/cron.py>
<input name='n'>Enter name of the job</input>
<br>
<input name='p'>Enter minutes</input>
<br>
<input name='q'>Enter hour</input>
<br>
<input name='r'>Enter day</input>
<br>
<input name='s'>Enter the syntax of the job</input>
<br>
<input type='submit'></input>
''')


