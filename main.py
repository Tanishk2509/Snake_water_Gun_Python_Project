import random
'''1 for snake
2 for water
3 for gun
'''
computer = random.choice([2, 3, 1])
youstr = input("Enter you choice: ")
youDict = {"s": 1, "w": 2, "g": 3}
reverseDict = {1: "snake", 2: "water", 3: "gun"}

you =youDict[youstr]

print(f"you choice {reverseDict[you]}\nComputer choice {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer ==2 and you ==1):
        print("you win")

    elif(computer ==2 and you ==3):
        print("you Lose")

    elif(computer ==1 and you ==2):
        print("you lose")

    elif(computer ==1 and you ==3):
        print("you win")

    elif(computer ==3 and you ==2):
        print("you win")

    elif(computer ==3 and you ==1):
        print("you Lose")

    else:
        print("Something went wrong")