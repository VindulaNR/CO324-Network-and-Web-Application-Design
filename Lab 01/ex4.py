'''Lab01 ex4
	E/16/319 Rathnayake R.P.V.N'''
from dataclasses import asdict
from json import dumps
from dataclasses import dataclass
from typing import List, Dict
import json
import ex1		#import the ex1 to get the lord_course_registraion function


s1=ex1.load_course_registrations("data.txt")	#lord the list of Student object in to the s1
s1=(map(asdict,s1))								#aply asdict() to s1 my useng the map function

e=json.dumps(list(s1))							#convert into jsom=n string
#print(e)
with open("student_registrations.json","w") as f:		#open json file and write on it
	f.write(e)