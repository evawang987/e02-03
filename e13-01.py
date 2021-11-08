#Extracting Data from XML
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
#The program will prompt for a URL, read the XML data from that URL using urllib
#and then parse and extract the comment counts from the XML data,
#compute the sum of the numbers in the file.
#Actual data: http://py4e-data.dr-chuck.net/comments_1369873.xml (Sum ends with 87)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
lst = list()

url = 'http://py4e-data.dr-chuck.net/comments_1369873.xml'
print('Retrieving', url)
fh = urllib.request.urlopen(url).read()
print('Retrieved',len(fh),'characters')

tree = ET.fromstring(fh)
comment = tree.findall('.//comment')
for count in comment:
    count = int(count.find('.//count').text)
    lst.append(count)

print('Count:',len(lst))
print('Sum:',sum(lst))
