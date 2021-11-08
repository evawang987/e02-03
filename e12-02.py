#Scraping Numbers from HTML using BeautifulSoup
#In this assignment you will write a Python program similar urllink2.py.
#The program will use urllib to read the HTML from the data files below,
#and parse the data, extracting numbers and compute the sum of the numbers in the file.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1369871.html (Sum ends with 77)


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1369871.html', context=ctx).read()
soup = BeautifulSoup(fh, "html.parser")

count = 0
sum = 0
tags = soup('span')
for i in tags:
    num = int(i.contents[0])    #找到span 后面的bytes
    sum = sum + num
    count += 1

print('Count:', count)
print('Sum:', sum)
