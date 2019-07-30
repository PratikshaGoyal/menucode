#!/usr/bin/python36
import subprocess as sp
print("content-type: text/html")
print()
print('''
<style>
  .speech { margin-top: 10%; margin-left: 40%;  color: white;}
  body{
    margin:auto;
}
</style>
<body background="https://wallpapercave.com/wp/Kj5cd8B.jpg">
<form action=http://192.168.43.115/cgi-bin/serv.py>
<div class="speech">
<p>Enter name of the service</p>
<input name='n'></input>
<br>
<input type='submit'></input>
</div>
</form>
</body>
''')
