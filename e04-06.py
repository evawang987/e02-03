input_hour = input("Enter Hours:")
input_rate = input("Enter Rate:")
hour = float (input_hour)
rate = float (input_rate)
def computepay(h, r):
    if h >= 40:
        pay = 40*r+(h-40)*r*1.5
    else:
        pay = h*r
    return print("Pay",pay)
computepay(hour,rate)
