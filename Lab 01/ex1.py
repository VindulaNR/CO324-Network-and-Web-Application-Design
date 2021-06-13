'''Lab1 CO324 ex1
E/16/319'''
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Student:

    """A student's course registration details"""
    given_name: str
    surname: str
    registered_courses: List[str]

def load_course_registrations(filename: str) -> List[Student]:

    """ Returns a list of Student objects read from filename"""
    List=list() 	#define a List to add Student
    with open(filename) as f:	
        for line in f:
            data= line.strip().split(",")		#geting the data from each line
            given_name=data[0]
            surname=data[1]
            registered_courses=data[2:]
            Student1=Student(given_name,surname,registered_courses)	#put them in to the Student data class
            List.append(Student1)		#create a list with student objects
    return List


student_list=(load_course_registrations("data.txt"))
#print(student_list)
#for obj in List: 
    #print( obj.surname, obj.given_name ) 
