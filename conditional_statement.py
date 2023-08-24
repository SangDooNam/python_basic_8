'''
Task 1 - calculate sum :
Your task is to write a Python program to calculate 
the sum of three integers given (prompted) by user.
If the values are equal then calculate triple value of their sum.
Print out an appropriate message to the user.
'''
# def IntFloatChanger(prompt):
#     while True:
#         value = input(prompt)
#         try:
#             return int(value)
#         except ValueError:
#             try:
#                 return float(value)
#             except ValueError:
#                 print('Enter a valid Number !')

# num1 = IntFloatChanger('Enter first Number : ')

# num2 = IntFloatChanger('Enter second Number : ')

# num3 = IntFloatChanger('Enter third Number : ')



# result1 = num1 * num2 + num3
# result2 = num1 + num2 + num3

# if num1 == num2 == num3:
#     print('If the given numbers are equl. they will be calculated triple and this is the result :', result1 )
# else:
#     print('The sum of the given numbers is : ', result2)

'''
Task 2 - get the difference :
Your task is to write a Python program to get 
the difference between a two given numbers (prompted by user).
If the first number is greater than second 
then calculate double difference between numbers.
Otherwise calculate the absolute difference between numbers.
Print out an appropriate message to the user.
'''
# def FloatInt(prompt):
#     while True:
#         value = input(prompt)
        
#         try:
#             return int(value)
#         except ValueError:
            
#             try:
#                 return float(value)
#             except ValueError:
                
#                 print('This is not valid number.')


# num1 = FloatInt('First number : ')
# num2 = FloatInt('Second number : ')

# difference = num1 - num2

# if num1 > num2:
#     print('The result of calculation is : ', difference ** 2 )
# else:
#     print('The result of calculation is : ', abs(difference) )
    
'''
Task 3 - odd or even number : 
Your task is to write a Python program to find whether a given number 
(prompted from the user) is even or odd. Print out an appropriate message to the user.
'''

# def floatANDint(prompt):
#     while True:
#         value = input(prompt)
#         try:
#             return int(value)
#         except ValueError:
#             try:
#                 return float(value)
#             except ValueError:
#                 print('Enter a valid number')
            
# num = floatANDint('Number to check : ')

# if num % 2 ==0:
#     print(num, 'is an even Number!!')
# else:
#     print(num, 'is an odd number!!')

# '''
# Task 4 - circle area : 
# Your task is to write a Python program which accepts 
# (prompts) the float radius of a circle from the user and compute its area.
# Round the result to two decimals!
# Print out an appropriate message to the user.
# '''
# import math

# def floatAndInt(prompt):
#     while True:
#         value = input(prompt)
#         try:
#             return int(value)
#         except ValueError:
            
#             try: 
#                 return float(value)
#             except ValueError:
#                 print('This is not a valid number. ')

# num = floatAndInt(" I'm a circle area calculator. Please enter a radius. :" )

# print('The area of the circle with the given radius is :', round(math.pi * num **2, 2))

'''
Task 5 - guess a number :
Your task is to write a Python program to guess a number between 1 to 10.
'''


# def intDiscriminator(prompt):
#     while True:
#         value = input(prompt)
#         try:
#             return int(value)
#         except ValueError:
#             print('Enter an integer')

# secrectNum = 27

# guessedNum = intDiscriminator('Guess the hidden number between 1 and 100 : ')

# while True:
    
#     if guessedNum == secrectNum:
#         print ('You got it. ')
        
#         break
        
#     elif guessedNum > secrectNum:
        
#         guessedNum = intDiscriminator('The given number is greater than the hidden number. : ')
        
#     elif guessedNum < secrectNum:
        
#         guessedNum = intDiscriminator('The given number is less than the hidden number. : ')
        

'''
Task 6 - Celsius to Fahrenheit conversion : 
Your task is to write a Python program to convert 
temperatures to and from Celsius, Cahrenheit.
In the centigrade scale, which is also called 
the Celsius scale, water freezes at 0 degrees and boils at 100 degrees.
In the Fahrenheit scale, water freezes at 32 degrees and boils at 212 degrees.
'''

# def intAndfloat(prompt):
#     while True:
#         value = input(prompt)
#         try:
#             return int(value)
#         except ValueError:
#             try:
#                 return float(value)
#             except ValueError:
#                 print('This is not valid number. ')

# celsiusOrFahrenheit = input("Input the scale shortcut you'd like to convert ('F' - Fahrenheit, 'C' - Celsius: ")

# while True:

#     if celsiusOrFahrenheit == 'c' and 'C':
#         CtoF = intAndfloat(" You input 'C', so I will convert from Celsius to Fahrenheit. \n Please type in the temperature in Celsius: ")
        
#         print('The temperature in Fahrenheit is', round(CtoF * 9/5 + 32 , 2),'degrees' )
        
#         break

#     elif celsiusOrFahrenheit == 'F' and 'f':
#         FtoC = intAndfloat("You input 'F', so I will convert from Fahrenheit to Celsius. \n Please type in the temperature in Fahrenheit: ")
        
#         print('The temperature in Celsius is', round((FtoC -32) * 5/9, 2),'degrees')
        
#         break
    
#     elif celsiusOrFahrenheit != 'c' and 'C' and 'F' and 'f':
        
#         celsiusOrFahrenheit = input(" If you want to convert from Celsius to Fahrenheit, type 'C'. \n If you want to convert from Fahrenheit to Celsius, type 'F'. : ")


'''
Task 7 - pattern : 
Your task is to write a Python program to construct the following pattern.
Upper part should be done in one line of code without using a loop.
Lower part can be done with any kind of loop or also with one line of code and without loops.
'''

# print('*', '* *', '* * *', '* * * *', '* * * * *', sep='\n' )
# for i in ['* * * *', '* * *', '* *', '*' ]:
#     print(i)
    
    
# print(1 * '* ',2 * '* ',3 * '* ',4 * '* ',5 * '* ', sep='\n', )
# for i in [4 * '* ',3 * '* ',2 * '* ',1 * '* ' ]:
#     print(i)


''' Task 8 - Fibonacci series : 
Your task is to write a Python program to get the Fibonacci series between 0 to 50.
'''


# a, b = 0, 1
# count = 0
# while count < 10:
#         print(a)
#         a, b = b, a + b
#         count += 1





