#Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case. Use the file words.txt to produce the output below.

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    quit()

content_o = fhand.read()
content_u = content_o.upper()
content_c = content_u.rstrip()
print(content_c)

#OR
for lx in fhand:
    ly = lx.rstrip()
    print(ly.upper())
