import random

number1 = random.randint(1,100)
i = 0
k = 0
while True:
    number2 = input("Enter number or q if you want to finish: ")
    if number2 == "q" or number2 == "Q":
        print("The end")
        break
    elif number1 == int(number2):
        print("You win")
        break
    else:
        print("You lost")
        k +=1
    i +=1
print(number1)
print("Number of attempts: ", k)