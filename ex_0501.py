#5.1

tot=0.0
ct=0
while True:
    sval=input('Enter a number: ')
    if sval=='done':
        break
    try:
        fval=float(sval)
        #print (fval)
    except:
        print('Invalid input')
        continue
    
    tot=tot+fval
    ct=ct+1

print(tot,ct,tot/ct)