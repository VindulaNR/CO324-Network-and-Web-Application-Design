#Lab03 excersice 3 part b
from urllib import request

def spider_metadata(urls: list):
	#creat a list for return value
	heads=list()
	#o through every url in the list
	for a in urls:
		#get the respons by reqursting
		response = request.urlopen(a)
		#gett the headers
		head=response.headers.items()
		#append it to the list
		heads.append(head)
	return heads

#print(spider_metadata(["http://www.pdn.ac.lk/"]))