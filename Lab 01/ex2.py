'''Lab01 ex2
	E/16/319 Rathnayake R.P.V.N'''
#import the ex1 to get the load_cours_registration function
import ex1

#call the function in exsersice 1
student_list=ex1.load_course_registrations("data.txt")

#created the sorted list acording to the surname+given_name
sorted_list1=sorted(student_list, key = lambda s: s.surname + s.given_name) 
print(sorted_list1,"\n")

#sorthing the list acording to the number of registered courses
sorted_list2=sorted(student_list, key= lambda s:len(s.registered_courses))
print(sorted_list2)