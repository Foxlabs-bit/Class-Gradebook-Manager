#Class gradebook manager main python script

import time
import os
import sys
import requests
import colorama
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
font_color = Fore.WHITE

all_scores = []


def CS():
     os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
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
    
    # Wrapped in try/except so typing letters or long numbers doesn't crash it
    try:
        input_choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        time.sleep(1.5)
        display_menu()
        return

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
    elif input_choice == 8:
        Exit()
    elif input_choice >= 9:  # Safely placed before the final else block
        print("Bro why")
        time.sleep(1.5)
        display_menu()
    else:  # Catches negative numbers or other unexpected inputs
        print("Invalid option.")
        time.sleep(1.5)
        display_menu()


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
        student_number = 0
        print("Scores:")
        for score in scores:
            student_number += 1
            print("Student " + str(student_number)+ ": " + str(score)) 
        input_choice = input("Press enter to return to the main menu: ")
        if input_choice == "":
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
    print("The lowest score is: " + str(lowest_score))
    print("The highest score is: " + str(highest_score))
    print("==============================")
    exit_choice = input("Press enter to return to the main menu: ")
    if exit_choice == "":
        display_menu()

def passing_students(scores):
    CS()
    if not scores:
        print("No scores recorded yet")
        exit_choice = input("Press enter to return to the main menu: ")
        if exit_choice == "":
            display_menu()
    else:
        print("The students that pass are:")
        passing_count = 0
        for score in scores:
            if score >= 50:
                passing_count += 1 
                print(str(score))
        print("Total passing students: " + str(passing_count))
        input_choice = input("Press enter to return to the main menu")
        if input_choice == "":
            display_menu()

def change_font_color():
    global font_color
    CS()
    print("=====================================================")
    print("Change font color")
    print("=====================================================")
    print("1. Red")
    print("2. Blue")
    print("3. Green")
    print("4. Yellow")
    print("5. Magenta")
    print("6. White")
    print("7. Cyan")
    print("8. Back")
    choice = int(input("Choose a font color or exit: "))
    if choice == 1:
        font_color = Fore.RED
    elif choice == 2:
        font_color = Fore.BLUE
    elif choice == 3:
        font_color = Fore.GREEN
    elif choice == 4:
        font_color = Fore.YELLOW
    elif choice == 5:
        font_color = Fore.MAGENTA
    elif choice == 6:
        font_color = Fore.WHITE
    elif choice == 7:
        font_color = Fore.CYAN
    elif choice == 8:
        settings()
    else:
        print("Invalid choice!")
        time.sleep(0.8)
        change_font_color()
        return

    print(font_color + "Font color sucessfully changed")

def settings():
    CS()
    print("====================================================")
    print("Settings")
    print("====================================================")
    print("Version: Beta v1")
    print("1. Change font color")
    print("2. Main menu")
    exit_choice = int(input("Type a number: "))
    if exit_choice == 1:
        change_font_color()
    elif exit_choice == 2:
        display_menu()
    else:
        print("Oops bad input, try again!")
        time.sleep(0.8)
        settings()



def Exit():
    sys.exit()


# Start the program
display_menu()