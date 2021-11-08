#The program will use urllib to read the HTML from the data files below,
#extract the href= vaues from the anchor tags,
#scan for a tag that is in a particular position relative to the first name in the list,
#follow that link and repeat the process a number of times and report the last name you find.
#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Caitlinn.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: L

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter-')
count = int(input('Enter count:'))
position = int(input('Enter position:'))

print('Retrieving:',url)
for i in range(count):
    fh = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(fh, 'html.parser')
    tag = soup('a')
    url = tag[position-1].get('href',None)
    print('Retrieving:',url)
