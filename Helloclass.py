print('Hello class')

# This program displays the following
              
#Floating-point numbers in a column
              
#with their ecimal points alinged
              
num1 = 127.899
              
num2 = 3465.148
              
num3 = 3.776
              
num4 = 264.821
              
num5 = 88.081
              
num6 = 799.999
              
#Display each number in a field of 7 spaces
              
# with 2 decimal planes
              
print(format (num1, '7.2f'))
print(format (num2, '7.2f'))
print(format (num3, '7.2f'))
print(format (num4, '7.2f'))
print(format (num5, '7.2f'))
print(format (num6, '7.2f'))

# This program demonstrates how a floating-point
# number can be displayed as currency.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Your annual pay is ', \
      format(annual_pay, ',.2f'), \
      sep=' :$')
             
# Get the user's name, age and income.
name = input('What is your name? ')
age = int(input('What is your age? '))
income = float(input('what is your income? '))

# Display the data.
print('Here is the data you entered:')
print('Name:', name)
print('Age:', age)
t=age+10
print('you age after 10 years', t )
print('Income:', income)


