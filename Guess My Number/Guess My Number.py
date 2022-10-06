# Ethan Farnsworth
# 09.26.22
# Guess My Number



# import
import random


# global vars

min = 1
max = 10
number = 0
guess = 0
tries = 3


# main
def checkforIntInput(question,min,max):
    """get a good number within a given range and validate the data before it returns it"""
    number =""
    while(True):
        number = input(question)
        if(number.isdigit()) and ((int(number) < max) and (int(number) > min)):
            number = int(number)
            return number

        else:
            print("not a good input")

def main():
# The same variables that are in global vars, however for some reason
# they only work inside of def main.
    min = 0
    max = 0
    number = 0
    guess = 0
    tries = 0
    playing = True

    while playing:
        while True:
            diff = input("Pick your difficulty; Easy, Medium, or Hard?: ")
            if(diff in ["Easy","easy","EASY","e","E","1"]):
                min = 1
                max = 10
                tries = 3
                break
            elif(diff in ["Medium","medium","MEDIUM","m","M","2"]):
                min = 1
                max = 300
                tries = 5
                break
            elif(diff in ["Hard","hard","HARD","h","H","3"]):
                min = 1
                max = 1000
                tries = 10
                break

            else:
                print("not a good input")


    # It chooses a random number within the given range (defined by min,max),
        number = random.randint(min,max)
        guess = checkforIntInput("Pick a number between " + str(min)+" and " + str(max) +"!: ",min,max)
        while(guess != number and tries>1):
            if(guess < number):
                print("Guess Higher: ")
                tries -= 1
            elif(guess > number):
                print("Guess Lower: ")
                tries -= 1
            checkforIntInput("Pick a number between " + str(min) + " and " + str(max) +"!: " ,min,max)

        if(tries > 1):
            print("You got it!")
        else:
            print("You suck at this!!")
        answer = input("Want to play again?: y or n")
        if("n" in answer.lower()):
            playing = False

    main()