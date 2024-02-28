import random as r
attempts=0
def difficulty():
    global attempts
    d=input("choose the level of difficulty easy or hard :")
    if d=="hard":
        attempts=5
    else:
        attempts=10


difficulty()

number=r.randint(1,100)

def users_guess(guess):
    global attempts,number
    if guess>number:
        print("too high")
        attempts-=1
   
    elif guess<number:
        print("too low")
        attempts-=1
        
    elif guess==number:
        print("you guessed correct number")
        print("you wIn")

while attempts>0 :
    print(f"you have {attempts} attempts ")
    guess = int(input("guess the number :"))
    users_guess(guess)