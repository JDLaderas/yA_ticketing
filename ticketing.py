
print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("For young age. Please pay $5.")
        bill = 5
    elif age < 18:
        print("For youth. Please pay $7.")
        bill = 7
    elif age <= 44:
        print("For adult. Please pay $12.")
        bill = 12
    elif age >= 45 or age <= 59:
        print("It's ok, you can ride for free.")
        bill = 0
    else:
        print("You are senior citizen, please hop in!")
        bill = 0

    photo = input("Do you want to add a photo? Y or N? ")
    if photo == "Y" or photo == "y" or photo == "yes" or photo == "YES" or photo == "Yes":
        bill += 3
        print(f"The total bill is ${bill}.")
    else:
        bill = bill
        print(f"The total bill is ${bill}.")
else:
    print("Sorry, you can't ride!")
