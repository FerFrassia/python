import urllib2

response = urllib2.urlopen('http://python.org/')

print 'Response: ',response
print 'The URL is: ',response.geturl()
print 'This gets the code: ',response.code
print 'The headers are: ',response.info()
print 'The date is: ',response.info()['date']
print 'The server is: ',response.info()['server']

html = response.read()
print 'Get all data: ',html
print 'Get the length: ',len(html)

for line in response:
	print line.rstrip()