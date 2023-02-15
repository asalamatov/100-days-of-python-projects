from art import logo
from os import system

print(logo)
print("Welcome to the Secret Auction program.")
dict = dict()

def find_highest_bid(bidding_record):
    max_bid = 0
    max_name = ""
    for k in bidding_record.keys():
        if bidding_record[k]>max_bid:
            max_bid = bidding_record[k]
            max_name = k
    print(f"The winner is {k} with a bid of ${max_bid}.")

continue_program = True
while continue_program:
    name = input("What is you name?: ")
    dict[name]=int(input("What is your bid?: $"))
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower().strip()
    if should_continue == "no":
        continue_program = False
    elif should_continue == "yes":
        system("cls")
find_highest_bid(dict)


