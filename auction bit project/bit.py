from art import logo
from replit import clear
auction_bid={}
go=1

while(go):
    print(logo)
    name=input("Enter your name:")
    bit=int(input("Enter your bid:Rs"))
    auction_bid[name]=bid
    con=input("type 'yes to continue . type 'no' to end :")
    if con=="no":
        go=False
        print("Good bye")
    else:
        clear()
max=0
print(auction_bid)
for n in auction_bid:
    if auction_bid[n]>max:
        max=auction_bid[n]
for n in auction_bid:
    if auction_bid[n]==max:
        print(f"the winner is {n} with the bid of {auction_bid[n]}")
        print("the auction is over, Thanks for joining")
