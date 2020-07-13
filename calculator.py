import definitions
import math

# The line above will let you separate your concerns by defining functions your calculator might use in a separate file.
def years1(principal,goal,bank):
   return math.log(goal/principal,1+rates[bank])


rates = {
    "TD": .0005,
    "Chase": .0003,
    "Bank of America": .0002,
    "Citi Bank": .0003,
    "Wells Fargo": .0004
}

def balance1(principal, bank, years):
    for i in range(0, years): 
        interest = principal * rates[bank]
        principal += interest 
    deposit = principal
    print("the balance for the year is " + (str(round((principal),2))))


print("welcome to your budget calculator")
deposit = float(input("How much money do you want to deposit?"))
bank = input("What is your bank?")


years = input("Do you know how many years you want to save for. y/n")
if years == "y":
    years= int(input("How many years do you want to save for?"))
    balance1(deposit, bank, years)
else:
    goal = float(input("How much money would you like to have?"))
    print("You have to wait " + str(round(years1(deposit, goal, bank))) + " years")

