'''For this mini project, I will write a program that allows users to (1. Convert Dollars to Peso) and (2. Determine if the \
economy for a certain day is good or bad.)'''
    
'''Since the conversion only uses multiplication function, we can define the currencies in terms of x and y.'''

def multiply(x, y):
    return x * y

# On this part, the program will going to ask the user if what mode he/she wants it to do. 
print('Select Mode.')
print('1. Currency Converter.')
print('2. Economy Checker')

while True:
    option = input("Enter the mode you want (1/2): ")
    
    if option == '1':
        num1 = float(input('Enter the Dollar Value for Today: '))
        num3 = float(input('Enter the Peso Value: '))
        print(num1, "*", num3, "=", multiply(num1, num3))
        break


    
    if option == '2': 
        num1 = float(input('Enter the Dollar Value for Today: '))
        num2 = float(input('Enter the Dollar Value Yesterday: '))
    
            
        if num1 < num2:
            print('The Economy Report for today is good.')
            break
            
        else: 
            print('The Economy Report for today is bad.')
            break
            
            
    if option != ('1' or '2'):
        print('Invalid Input!')
        break
    
            
    


        
    
    
        
