import random 
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
youstr = input("enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1: "snake",-1: "water", 0: "gun"}

you = youDict[youstr]

#by now we have 2 nos you and computer

print(f" you chose{dict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

if((computer - you)== -1 or (computer - you)== 2):
    print("you lose")
else:
    print("you win")