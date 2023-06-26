#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

numbers=[] #created the list for numbers
while True:
    num=input('Enter an integer: ')
    if num=='done':
        break
    try:
        number=int(num)
    except:
        print('Invalid input')
        continue
    numbers.append(number) #append enters the input(converted to integers) into the number list

smallest=numbers[0]
largest=numbers[0]

for number in numbers:
    if number<smallest:
        smallest=number
    if number>largest:
        largest=number

print('Maximum is',largest)
print('Minimum is',smallest)