import random
from data import data
from replit import clear

def compare(a,b):
    if a['follower_count']>b['follower_count']:
        return "a"
    elif a['follower_count']<b['follower_count']:
        return "b"
    else:
        return "b"

def game():
    flag=True
    score=0
    while flag:
        a=random.choice(data)
        b=random.choice(data)
        print(f"team A = {a['name']}, is a {a['description']} , from {a['country']}")
        print(f"team B = {b['name']}, is a {b['description']} , from {b['country']}")
        guess=input("who do u think has higher followers on instagram : ")
        choice=compare(a,b)
  
        if guess==choice:
            print("your right")
            score+=1
            clear()
        else:
            print("your wrong")
            print(f"final score= {score}")
            flag=False

game()

