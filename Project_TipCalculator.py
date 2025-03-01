# Printing Proper
print("Welcome to the tip calculator!")

# Input statements set-up
total = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
split = float(input("How many people to split the bill? "))

# Formula Setup
percentage = total * (tip / 100)
total_tip = (total + percentage) / split
rounding = round(total_tip, 2)

# Output
print(f"Each person should pay: ${rounding}")


