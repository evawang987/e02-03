#Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list
#and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.

fname = input('Enter a file name:')
fh = open(fname)
content = fh.read()
content = content.rstrip()
output = list ()
for la in content:
    la = content.split()
    for i in la:
        if i in output:
            continue
        else:
            output.append(i)

output.sort()
print(output)


#通过set()集合去除重复值，la = list(set(la))
