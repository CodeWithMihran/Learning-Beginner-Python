import random


compChoice = random.choice([1, 0, -1])

yourChoice = input("Enter your choice : ")
gameRule = { "s":1, "g":0, "w":-1}
revRule = { 1:"Snake", -1:"Water", 0:"Gun"}

you = gameRule[yourChoice]
print(f"You Choose : {revRule[you]}\nComputer Choose : {revRule[compChoice]}")

if(you == compChoice):
    print("Its a draw")

else:
    if(compChoice == -1 and you == 1):
        print("You win")

    elif(compChoice == -1 and you == 0):
        print("You Lose")

    elif(compChoice == 1 and you == -1):
        print("You Lose")

    elif(compChoice == 1 and you == 0):
        print("You Win")

    elif(compChoice == 0 and you == -1):
        print("You Win")

    elif(compChoice == 0 and you == 1):
        print("You Lose")               

    else:
        print("Something went wrong !!")    