import random

MENU = """"G - get a valid score 
P - print result 
S - show stars 
Q - quit"""

def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
            print(score)
        elif choice == "P":
            score = float(input("Enter score: "))
            print(determine_score)
        elif choice == "S":
            score = float(input("Enter score: "))
            print("*" *int (input("Enter score: ")))
        else:
            print("Invalid option")
        print(MENU)
    print("Thank you.")





def determine_score():
    if SCORE_MIN < score < SCORE_MID:
        level = "Bad"
    elif score < SCORE_HIGH:
        level = "Pass"
    elif score < SCORE_MAX:
        level = "Excellent"
    else:
        level = "Invalid score"

    print(level)




main()




