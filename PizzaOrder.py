print("Welcome to Shakey's Pizza Parlor Deliveries!")
size = input("What size of pizza do you want? |S|M|L|: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")

bill = 0

# How much they need to pay based on their size choice | S = $15 | M = $20 | L = $25
if size == "S": 
    bill = 15
elif size == "M": 
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Check whether you typed the correct input.")

# How much to add to their bill based on their pepperoni choice | $2 |
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    print("Check whether you typed the correct input.")

# Final amount whether they want an extra cheese | $1 |
if extra_cheese == "Y":
    bill += 1
else:
    print("Check whether you typed the correct input.")

print(f"Your bill is ${bill}.")
