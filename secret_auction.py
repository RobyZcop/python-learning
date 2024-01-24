# Here focus on dictionaries

from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bidders = []

def add_bidder(bidder_list, bidder_name, bidder_price):
    bidder_dict = {"name": bidder_name, "price": bidder_price}
    bidders.append(bidder_dict)

def check_winner(total_bidders):
    highest_bid = 0
    winner = ""
    for bidder in total_bidders:
        if bidder["price"] > highest_bid:
            highest_bid = bidder["price"]
            winner = bidder["name"]
    print(f"The winner is {winner} with a bid of ${highest_bid}")

is_more_people = True
while is_more_people:
    name = input("What is your name?: ")
    price = int(input("What is your bid price?: $"))
    add_bidder(bidders, name, price)
    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if other_bidders == "no":
        is_more_people = False
        check_winner(bidders)
    else:
        clear()
  
