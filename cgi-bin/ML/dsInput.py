#!/usr/bin/python36

print("content-type: text/html")
print()

import subprocess as sp

import sklearn 

from sklearn.externals import joblib

print("<b> Enter  model name:  </b>")
print("<br>")

print("""
<a href="http://192.168.43.115/cgi-bin/ML/askData.py?model=startup.sav">Startup Prediction </a>
<br/>

<a href="http://192.168.43.115/cgi-bin/ML/salaryData.py"> Salary Prediction</a>
<br/>
""")




