print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15%? %"))
no_of_people = int(input("How many people to split the bill? "))
amount_per_person = (total_bill*(1+tip/100))/no_of_people
print(f"Each person should pay: $ {amount_per_person}")