''' This is a GWA Calculator '''
# s -> refers to the final grade in the subject. 
# u -> refers to the total number of units. 
# p -> refers to the product of the grade and total number of units
# gwa -> refers to the gwa. 

print('Good day! Welcome to my GWA Calculator!' )
print('Wherever you are, I hope you are doing fine. Let us ace everything with our own greatness! ')


try: 
    s1 = float(input('Enter your grade in subject 1: '))
    u1 = int(input('Enter the total number of units in subject 1: '))
    p1 = s1 * u1
    
    s2 = float(input('Enter your grade in subject 2: '))
    u2 = int(input('Enter the total number of units in subject 2: '))
    p2 = s2 * u2
    
    s3 = float(input('Enter your grade in subject 3: '))
    u3 = int(input('Enter the total number of units in subject 3: '))
    p3 = s3 * u3
    
    s4 = float(input('Enter your grade in subject 4: '))
    u4 = int(input('Enter the total number of units in subject 4: '))
    p4 = s4 * u4
    
    s5 = float(input('Enter your grade in subject 5: '))
    u5 = int(input('Enter the total number of units in subject 5: '))
    p5 = s5 * u5
    
    s6 = float(input('Enter your grade in subject 6: '))
    u6 = int(input('Enter the total number of units in subject 6: '))
    p6 = s6 * u6
    
    s7 = float(input('Enter your grade in subject 7: '))
    u7 = int(input('Enter the total number of units in subject 7: '))
    p7 = s7 * u7
    
    s8 = float(input('Enter your grade in subject 8: '))
    u8 = int(input('Enter the total number of units in subject 8: '))
    p8 = s8 * u8
    
    s9= float(input('Enter your grade in subject 9: '))
    u9 = int(input('Enter the total number of units in subject 9: '))
    p9 = s9 * u9
    
    '''
    s10= float(input('Enter your grade in subject 11: '))
    u10 = int(input('Enter the total number of units in subject 11: '))
    p10 = s9 * u9'''
    
    '''
    s11= float(input('Enter your grade in subject 11: '))
    u11 = int(input('Enter the total number of units in subject 11: '))
    p11 = s11 * u11
    '''
    
    units = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8 + u9
    grades = (p1 + p2 + p3 + p4 + p5  + p6 + p7 + p8 + p9) 
    gwa = grades / units 
    
    result = print('Your GWA is', gwa)

  
    
except: 
    print('Invalid input! Please enter a valid grade. ')
    
              


    
    
    
    
    
    
    
    