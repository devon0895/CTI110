#DevonPoole
#4/30/2024
#P5LAB
#Use of loops, functions and module import to complete assignments

import random

def addsum():
    num1 = random.randint(1, 100)

    num2 = random.randint(1, 100)

    num3 = num1 + num2

    print(f" {num1} + {num2} = ?")
    guess = int(input("Enter answer. "))

    tries = 1

    while guess != num3:
        print("Incorrect, try again")
        if guess > num3:
              print("Sorry, your answer is too high.")
        if guess < num3:
              print("Sorry, your answer is too low.")
        guess = int(input("Enter answer. "))
        tries += 1

    print("Congratulations, your answer is correct!")
    print(f"Number of guesses: {tries}")




def subdiff():

    num1 = random.randint(1, 100)

    num2 = random.randint(1, 100)

    num4 = num1 - num2

    tries = 1

    print(f" {num1} - {num2} = ?")
    guess = int(input("Enter answer."))

    while guess != num4:
        print("Incorrect, try again")
        if guess > num4:
              print("Sorry, your answer is too high.")
        if guess < num4:
              print("Sorry, your answer is too low.")
        guess = int(input("Enter answer. "))
        tries += 1

    print("Congratulations, your answer is correct!")
    print(f"Number of guesses: {tries}")
            

def main():
    
    print("Welcome to Math Quiz")



    print("MAIN MENU")

    print("--------------" * 2)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

    option = input("Enter an option: ")

    while option != "3":

        if option == "1":
            addsum()

        if option == "2":
            subdiff()
        option = input("Enter an option: ")
    print("Thank you for playing.")
main()

                    





                        

                        

