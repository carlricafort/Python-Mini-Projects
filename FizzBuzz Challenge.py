'''This program is all about the classic Fizz Buzz Challenge'''

'''If the number is a multiple of 3, you need to print "Fizz" instead of that number.'''
''''If the number is a multiple of 5, you need to print "Buzz" instead of that number.'''
'''If the number is a multiple of both 3 and 5, you need to print "FizzBuzz" instead of that number.'''

try: 
    user_input = int(input("Enter a whole number: "))
    
    if user_input%3 == 0 and user_input%5 == 0:
        print('FizzBuzz')
        
    elif user_input%3 == 0:
        print('Fizz')
        
    elif user_input%5 == 0:
        print('Buzz')
    
    else:
        print('The number is not divisible by 3 nor 5')


except:
    print("Error: Your input is not a whole number!")
