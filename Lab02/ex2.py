from urllib import request
from urllib import parse

with request.urlopen("https://www.duckduckgo.com/?q=Rocco's+basilisk&ie&format=json&pretty=1") as query:
	body = query.read()
	print(body)
	print(type(body))