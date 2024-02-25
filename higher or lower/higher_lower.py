import random
from data import data

a=random.choice(data)
b=random.choice(data)
print(a)
print(f"team A = {a['name']}, is a {a['description']} , from {a['country']}")
print(b)
print(f"team B = {b['name']}, is a {b['description']} , from {b['country']}")

def compare(a,b):
    if a['follower_count']>b['follower_count']:
        return True
    else:
        return False

def game(a,b):
    guess=input("who do u think has higher followers on instagram : ")
    if guess=="a" or guess=="A":
        if compare(a,b):
            print("your right")
        else:
            print("your wrong")

game(a,b)

