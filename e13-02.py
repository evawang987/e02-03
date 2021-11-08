#Extracting Data from JSON
#In this assignment you will write a Python program somewhat similar to json2.py.
#The program will prompt for a URL, read the JSON data from that URL using urllib
#and then parse and extract the comment counts from the JSON data,
#compute the sum of the numbers in the file and enter the sum below:
#Actual data: http://py4e-data.dr-chuck.net/comments_1369874.json (Sum ends with 24)

import urllib.request, urllib.parse, urllib.error
import json

count = 0
sum = 0

url = 'http://py4e-data.dr-chuck.net/comments_1369874.json'
print('Retrieving from',url)
data = urllib.request.urlopen(url).read()
print('Received', len(data),'characters')

info = json.loads(data)
for i in info["comments"]:
    num = int(i["count"])
    sum = sum + num
    count += 1

print('Count:',count)
print('Sum:',sum)
