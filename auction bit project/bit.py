from art import logo
from replit import clear
auction_bid={}
go=1
def auction(auction_bid):
    winner=""
    max=0
    for n in auction_bid:
       if auction_bid[n]>max:
           max=auction_bid[n]
           winner=n
    print(f"the winner is {winner} with a bid of Rs{max}")
    
while(go):
    print(logo)
    name=input("Enter your name: ")
    bid=int(input("Enter your bid: Rs"))
    auction_bid[name]=bid
    con=input("type 'yes to continue . type 'no' to end : ")
    if con=="no":
        go=False
        auction(auction_bid)
        print("Good bye")
    else:
        clear()


