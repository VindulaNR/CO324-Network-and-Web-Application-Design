CO324 Lab 1: Python crash course part II

Objective
Review some basic concepts of programming in Python including: input-output, using data structures, OOP and generators.

Preparation
Install Python version 3.7 or newer on your computer. You may use whichever IDE or editor that you prefer.

Instructions
From this lab onwards, submissions that do not follow instructions will incur a 10% penalty.

Use only the standard built-in modules in Python to complete these exercises.
Put the solutions to coding exercises in files named ex1.py, ex2.py, etc.
Solutions to short answer questions should be in a single plain text file named answers.txt. State your E-number at the top of answers.txt.
Zip all your files and submit them (please don’t use other formats.)
References
Python data classes: https://realpython.com/python-data-classes/

JSON in Python: https://realpython.com/python-json/

Exercises

A text file contains student course details. Each line contains first and last names, and a list of courses that they have completed separated by commas.
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

Read the file into a list of Student objects using the above definition.

We can use the built-in sorted function to sort the list by surname and given name.
sorted(student_list, key = lambda s: s.surname + s.given_name)

How would you sort students by the number of courses that they are registered for? (Hint: look at the len function)

Suppose we want to look up student information by name.
Store Student objects in a dictionary using a tuple (surname, given_name) as the key.
Can we use a two-element list [surname, given_name] as the key? Explain why.

JSON is a common format for exchanging data between web APIs. We can serialise our Student class as JSON as follows.
from dataclasses import asdict

from json import dumps


s1 = Student("Saman","Silva",["CO324","CO321","CO325"])

dumps(asdict(s1))

Use Python’s `map` function to apply asdict() to a list of Student objects.
Use `json.dump` to write the output to a file named student_registrations.json.
