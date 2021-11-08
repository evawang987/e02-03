#Write a program that prompts for a file name, then opens that file and reads through the file,
#looking for lines of the form: X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines
#and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.

fname = input('Enter File Name:')
try:
    fh = open(fname)
except:
    print('File cannot be opened:',fname)
    quit()

count = 0
total = 0
for lx in fh:
    ly = lx.rstrip()
    if ly.startswith('X-DSPAM-Confidence:'):
        x = ly.find(':')
        num = float(ly[x+2:])
        count = count +1
        total = total + num
print("Average spam confidence:", total/count)
