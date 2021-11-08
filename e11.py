#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_1369869.txt (There are 76 values and the sum ends with 119)

import re

fh = open ('regex_sum_1369869.txt')
content = fh.read()
num = re.findall('[0-9]+',content)
print(num)
sum = 0
for i in num:
    sum += int(i)

print('Sum:', sum)
