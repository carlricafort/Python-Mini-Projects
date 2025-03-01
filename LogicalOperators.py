# Multiple if statements in succession

print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))
bill = 0


if height > 120:
    age = int(input("Enter your age: "))
    print("Can ride.")
    if age > 18 and age < 45: 
        bill = 12
        print("Please pay $12.")

    elif age >= 12 and age <=18:
        bill = 7
        print("Please pay $7.")
    
    elif age >= 45 or age <= 55:
        bill = 0
        print("Your bill is free.")

    else:
        bill = 5
        print("Please pay $5.")
    
    wants_photo = input("Do you want to have a photo take? Type y for YES and n for NO.")
    if wants_photo == "y":
        bill += 3 # Adding 3 dollars to the bill
        
    print(f"Your bill is ${bill}.")
else:
    print("Can't ride.")
