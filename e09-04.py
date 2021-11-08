#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fh = open ('mbox-short.txt')

y = list()
for lx in fh:
    if not lx.startswith("From:"): continue     #From的冒号不要漏掉！
    lx = lx.split()
    y.append(lx[1])

x = dict()
for i in y:
    x[i] = x.get(i,0) + 1

sender = None
feq = None
for k,v in x.items():
    if sender is None or v > feq:
        sender = k
        feq = v
print(sender,feq)


#OR
fh = open ('mbox-short.txt')

x = dict()
for lx in fh:
    if not lx.startswith('From'):continue      #找到句子
    lx = lx.split()         #变成list
    email = lx[1]
    x[email] = x.get(email,0) + 1

sender = None
feq = None
for k,v in x.items():
    if sender is None or v > feq:
        sender = k
        feq = v
print(sender,feq)
