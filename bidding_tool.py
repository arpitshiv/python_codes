
from replit import *
bid={}
bid_finished=False
def find_highest_bidder(bidding_records):
    highest_bid=0
    for bidder in bidding_records:
        bid_amount=bidding_records[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"the highest bidd is {highest_bid} and the winner is {winner}")

while not bid_finished:
    name=input("enter your name")
    price=int(input("enter your bid"))
    bid[name]=price
    should_continue=input("is there any other bidder type yes on no")
    if should_continue=="no":
        bid_finished=True
        find_highest_bidder(bid)
    elif should_continue=="yes":
        clear()

