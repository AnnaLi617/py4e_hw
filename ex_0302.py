#3.2 use try/except command to deal with traceback

hrs = input('Enter Hours: ')
h = float(hrs)
rate = input('Enter Hourly Rate: ')
try:
    rt = float(rate)
except:
    print('Error, please enter numeric input')
    exit()
    
if h <= 40:
    pay = h*rt
else:
    pay = 40*rt+(h-40)*1.5*rt

print(pay)


