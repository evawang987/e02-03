largest = None
smallest = None
while True:
    num = input('Enter a Number:')
    if num == 'done':
        break
    try:
        test = int(num)
        if largest is None or largest < test:
            largest = test
        if smallest is None or smallest > test:
            smallest = test

    except:
        print('Invalid input')
        continue


print('Maximum is', largest)
print('Minimum is', smallest)



#for x in num:
    #if x > largest:
    #    largest = x
#for y in num:
#    if y < smallest:
#        smallest = y
