'''Lab01 ex3
    E/16/319 Rathnayake R.P.V.N'''
from dataclasses import dataclass
from typing import List, Dict
from dataclasses import asdict
from json import dumps

@dataclass
class Student:

    """A student's course registration details"""
    given_name: str
    surname: str
    registered_courses: List[str]

def load_course_registrations(filename: str) -> List[Student]:

    """ Returns a list of Student objects read from filename"""
    List=dict() 	#define a List to add Student
    with open(filename) as f:	
        for line in f:
            data= line.strip().split(",")		#geting the data from each line
            given_name=data[0]
            surname=data[1]
            registered_courses=data[2:]
            Student1=Student(given_name,surname,registered_courses)	#put them in to the Student data class
            List[surname, given_name]=registered_courses		#create a dic with student objects,set the key
    return List

#List=load_course_registrations("data.txt")
#print(List['Thennakoon', 'Arjuna'])
