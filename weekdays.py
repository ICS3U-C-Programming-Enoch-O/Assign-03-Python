#!/usr/bin/env python3
# Created by: Enoch O
# Created on: April 1 2025
# This program Gets a number from the user and displays the corresponding weekday.
import math


def main():
    user_input_string = input("choose a num between 1-7: ")

    # assign user input to corresponding week
    try:
        user_input_int = int(user_input_string)
        if user_input_int < 1 or user_input_int > 7:
            print("please choose between 1-7")
        else:
            if user_input_int == 1:
                print("Monday")
            elif user_input_int == 2:
                print("Tuesday")
            elif user_input_int == 3:
                print("Wednesday")
            elif user_input_int == 4:
                print("Thursday")
            elif user_input_int == 5:
                print("Friday")
            elif user_input_int == 6:
                print("Saturday")
            elif user_input_int == 7:
                print("Sunday")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
