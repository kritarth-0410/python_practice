import random

computer = random.choice([-1,0,1])

a = input ("Enter your choice : ")
b = {"s" : 1, "w" : -1, "g" : 0}
c = {1 : "Snake", -1 : "water", 0 : "Gun"}

you = b[a]

print(f"You chose {c[you]} \n Computer chose {c[computer]}")

if(computer == you):
    print("draw")

else:
    if(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    elif(computer == 0 and you == -1):
        print("You Win!")
    else:
        print("Something Went Wrong")