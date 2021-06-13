from urllib import request

with request.urlopen("https://duckduckgo.com/?q=University+of+Peradeniya&format=json&pretty=1") as query:
	headers = query.headers.items()
	body = query.read()
	rahe=body.Results[0].FirstURL
	#rsult= body["Results"]
	data=body.decode("utf-8")
	print(list(query))
#print(data[RelatedTopics])
#print(rahe)

