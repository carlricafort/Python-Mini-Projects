# Thermal Expansion Calculator
# Note: This is only limited on solving the Delta L or the change in length of the material
    
# Input statements for the values needed like initial length of the material, Coefficient of Linear Expansion, and Temperatures needed
lo = float(input('The initial length of the material is: '))
alpha = float(input('The Linear Expansion Coefficient of the material is: '))
initial_temp = float(input('The Initial Temperature is: '))
final_temp = float(input('The Final Temperature is: '))

# The formula that we need in solving the thermal expansion of the material
delta_l = lo * alpha * ( final_temp - initial_temp )
print('The change in length is equal to: ', delta_l)

# <---------------------------------------------------------------------------------------------------->

# This propgram solves the initial length

# These are the input statements that we need in our calculator
delta_l = float(input('The Thermal Expansion of the material is: '))
alpha = float(input('The Linear Expansion Coefficient of the material is: '))
initial_temp = float(input('The Initial Temperature is: '))
final_temp = float(input('The Final Temperature is: '))

# The formula in solving the initial length of the material
lo = delta_l / (alpha * (final_temp - initial_temp))
print('The initial length of the material is: ', lo)

# <---------------------------------------------------------------------------------------------------->

# These are the input statements that we need in solving the coefficient of thermal expansion
delta_l = float(input('The Thermal Expansion of the material is: '))
lo = float(input('The initial length of the material is: '))
initial_temp = float(input('The Initial Temperature is: '))
final_temp = float(input('The Final Temperature is: '))

# Formula in solving the linear expansion coefficient
alpha = delta_l / (lo * (final_temp - initial_temp))
print('The Linear Expansion Coefficient of the Material is: ', alpha, '/ Celsius Degrees' )

# <---------------------------------------------------------------------------------------------------->

# These are the input statemetns that we need in solving for the initial temperature 
delta_l = float(input('The Thermal Expansion of the material is: '))
lo = float(input('The initial length of the material is: '))
alpha = float(input('The Linear Expansion Coefficient of the material is: '))
final_temp = float(input('The Final Temperature is: '))

# The formula that we need in solving for the initial temperature
initial_temp = (( lo * alpha * final_temp ) - delta_l) / (lo * alpha)
print('The Initial Temperature is', initial_temp, 'Degrees Celsius')

# <---------------------------------------------------------------------------------------------------->

delta_l = float(input('The Thermal Expansion of the material is: '))
lo = float(input('The initial length of the material is: '))
alpha = float(input('The Linear Expansion Coefficient of the material is: '))
initial_temp = float(input('The Initial Temperature is: '))

# The formula that we need in solving the Final Temperature is 
final_temp = (delta_l + (lo * alpha * initial_temp)) / (lo * alpha)
print('The Initial Temperature is', final_temp, 'Degrees Celsius')

# <---------------------------------------------------------------------------------------------------->
















