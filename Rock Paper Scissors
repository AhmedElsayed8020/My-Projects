import random

print("Rock:1 , Paper:2 , Scissors:3")
elements = ["Rock" , "Paper" , "Scissors"]
while True:
    try:
        player = int(input("Enter the number : "))
    except ValueError:
        print("Enter a number")
        continue
    if player in [1,2,3]:
        break
    else:
        continue
cpu = random.randint(1,3)

if (player == 1 and cpu == 1) or (player == 2 and cpu == 2) or (player == 3 and cpu == 3):
    print("player : " + elements[player - 1])
    print("cpu : " + elements[cpu - 1])
    print("Equal")

elif (player == 1 and cpu == 3) or (player == 2 and cpu == 1) or (player == 3 and cpu == 2):
    print("player : " + elements[player - 1])
    print("cpu : " + elements[cpu - 1])
    print("Win")
elif (player == 1 and cpu == 2) or (player == 2 and cpu == 3) or (player == 3 and cpu == 1):
    print("player : " + elements[player - 1])
    print("cpu : " + elements[cpu - 1])
    print("Lose")
