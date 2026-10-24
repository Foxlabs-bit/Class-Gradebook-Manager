#Class gradebook manager main python script

import time
import os
import sys
import colorama # will be used later for changing font color in settings

all_scores = []

def CS():
     os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    CS()
    #This is a basic loading bar i do not actually know how to make a proper one so this is a makeshift one for now and pray it looks good
    print("Loading")
    print("#####")
    time.sleep(0.1)
    CS()
    print("Loading")
    print("##########")
    time.sleep(0.1)
    CS()
    print("Loading")
    print("###############")
    time.sleep(0.1)
    CS()
    print("Loading")
    print("####################")
    time.sleep(0.1)
    CS()
    print("Loading")
    print("#########################")
    time.sleep(0.1)
    CS()
    print("Loading")
    print("##############################")
    time.sleep(0.1)
    CS()
    print("Loading")
    print("###################################")
    time.sleep(0.1)
    CS()
    print("Loading")
    print("########################################")
    time.sleep(0.1)
    CS()
    print("Loading")
    print("################################################")
    CS()
    print("====================================================")
    print("Welcome to Class Gradebook Manager V1")
    print("====================================================")
    time.sleep(0.5)
    print("1. Add a score")
    print("2. Show all scores")
    print("3. Class average")
    print("4. Letter grades")
    print("5. Highest and lowest scores")
    print("6. Count passing students")
    print("7. Settings")
    print("8. Exit")
    input_choice = int(input("Choose an option:"))
    if input_choice == 1:
        CS()
        addScores(scores=all_scores)
    elif input_choice == 2:
        CS()
        show_Scores(scores=all_scores)
    elif input_choice == 3:
        CS()
        average = calculate_Average(scores=all_scores)
        print("Class average:", average)
        input("Press Enter to return to the menu: ")
        display_menu()
    elif input_choice == 4:
        CS()
        grade = get_Letter_Grade(score=calculate_Average(scores=all_scores))
        input("Press Enter to return to the menu: ")
        display_menu()
    elif input_choice == 5:
        highest_and_lowest(scores=all_scores)
    elif input_choice == 6:
        passing_students(scores=all_scores)
    elif input_choice == 7:
        settings()
    else:
        Exit()


def addScores(scores):
    while True:
        try:
            score = str(input("Enter a score or type 'done' to finish: "))
            if score == str("done"):
                display_menu()
                break
            elif float(score) < 0 or float(score) > 100:
                print("Invalid score. Please enter a score between 0 and 100.")
            else:
                scores.append(float(score))
        except ValueError:
            print("Oops that is not a valid input!")
        except IndexError:
            print("Index out of range. please stop inputs.")
        except SyntaxError:
            print("Syntax Error. try again.")

def show_Scores(scores):
    if not scores:
        print("No scores to display. Add scores in 'Add a score'")
        time.sleep(2)
        display_menu()
    else:
        student_number = 1
        print("Scores:")
        for score in scores:
            print("Student " + str(student_number)+ ": " + str(score)) 
        exit_choice = input("Press enter to return to the main menu: ")
        if exit_choice == "":
            display_menu()

def calculate_Average(scores):
    if not scores:
        return 0 
    else:
        total = 0
        for score in scores:
            total += score
            division = total / len(scores)
    return division

def get_Letter_Grade(score):
    if score >= 90:
        print("A")

    elif score >= 80 and score < 90:
        print("B")

    elif score >= 70 and score < 80:
        print("C")

    elif score >= 50 and score < 70:
        print("D")
        
    else:
        print("F")

def highest_and_lowest(scores):
    lowest_score = min(all_scores)
    highest_score = max(all_scores)
    print("==========Statistics==========")
    print("The lowest score is: " + int(lowest_score))
    print("The highest score is: " + int(highest_score))
    print("==============================")
    exit_choice = input("Press enter to return to the main menu: ")
    if exit_choice == "":
        display_menu()

def passing_students(scores):
    #Need to choose a fitting pass score later!!!
    #Also practice this module when you get time!!! Very important to get this correct
    for score in scores < 60:
        print("Students that pass are: ")


def settings():


    print("====================================================")
    print("Settings")
    print("====================================================")
    print("Version: Beta v1")

def Exit():
    sys.exit()



display_menu()