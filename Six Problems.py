#file : Six Problems
#program: This Python program contains several interactive programs and a menu to choose among them. 
#         it provides a convenient way for users to interact with various utility programs
#         ranging from calculating grades, encrypting messages, and trying some mathematical concepts.
# Authors: 
#         Daad Amar Osman  | problems 3 and 4
#         Lina Mahmoud Ahmed  | prblems 2 and 5
#         Asrar Abdelgaber Osman | problems 1 and 6
          
#version: version 6
#Date: February 25th ,2024


def grades_calculator_program():
    # The grades calculator program
    def grades_calculator(mark):
        if mark >= 90:
            return "A+"
        elif mark >= 85:
            return "A"
        elif mark >= 80:
            return "B+"
        elif mark >= 75:
            return "B"
        elif mark >= 70:
            return "C+"
        elif mark >= 65:
            return "C"
        elif mark >= 60:
            return "D+"
        elif mark >= 50:
            return "D"
        else:
            return "F"

    print("\n                         WELCOME TO THE GRADE CALCULATOR PROGRAM!")                            
    print("This program takes your mark as input and calculates your grade based on a predefined scale.")
    name = input("\nFirst, may I know your name?\n ")
    print(f"Hello, {name}!")

    while True:
        try:
            mark = float(input("Please enter your mark: "))

            if 0 <= mark <= 100:
                grade = grades_calculator(mark)

                if grade in ("A", "A+"):
                    print(f"Excellent {name}! Your grade is {grade}.")
                elif grade in ("B", "B+"):
                    print(f"Very good {name}! Your grade is {grade}.")
                elif grade in ("C", "C+"):
                    print(f"Good {name}! Your grade is {grade}.")
                elif grade in ("D", "D+"):
                    print(f"Hmm, accepted {name}! Your grade is {grade}.")
                else:
                    print(f"Unfortunately {name}, you've got an {grade}. Try harder next time.")

                choice = input("\nDo you want to calculate another grade? (yes/no):\n ")

                if choice.lower() == "yes":
                    continue
                elif choice.lower() == "no":
                    print("\nThank you for using the Grade Calculator Program 🌟\n")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            else:
                print("Invalid mark. your mark should be between 0 and 100.\n")

        except ValueError:
            print("Invalid input. Please enter a valid number.\n")





def armstrong_number_program():
    # Function to check if a number is an Armstrong number
    def is_armstrong_number(num):
        num_str = str(num)
        num_digits = len(num_str)
        armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
        return armstrong_sum == num

    # Function to check if a number is positive
    def is_positive(num):
        return num > 0

    # Function to ask if the player wants to play again
    def play_again():
        while True:
            play = input("Do you want to play again? (yes/no): ").lower()
            if play == 'yes':
                return True
            elif play == 'no':
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    print("\n                         WELCOME TO AN ARMSTRONG NUMBER CALCULATOR")
    print("                 This Program checks if the entered number is an Armstrong Number.\n")

    while True:
        while True:
            num = int(input("\n Enter a number: "))
            if is_positive(num):
                break
            else:
                print("Please enter a positive number.")

        if is_armstrong_number(num):
            print(f"{num} is an Armstrong number ✅.\n")
        else:
            print(f"{num} is not an Armstrong number ❌.\n")

        if not play_again():
            print("\nThank you for playing 🌟\n")
            break




def pie_calculate_program():
    def calculate_pi(terms):
        pie = 1
        i = 2
        while i <= terms:
            pie = pie + ((-1) ** (i + 1)) * (1 / (2 * i - 1))
            i += 1
        pie = pie * 4
        return pie

    print('''
                                APPROXIMATION OF π

                This program will approximate the value of π using the 
             Leibniz series formula. The formula for the Leibniz series is:

                         π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
    ''')
    while True:
        try:
            terms = int(input("Please enter the number of terms for the approximation: "))
            if terms <= 0:
                print("Number of terms must be a positive integer.")
            else:
                print(f"\nThe Approximate value of π with {terms} terms is: {calculate_pi(terms)}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")





def encryption_program():
    def encrypt_message(message, shift):
        encrypted_message = ''
        for char in message:
            if char.isalpha():
                shifted = ord(char) + shift
                if char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                elif char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                encrypted_message += chr(shifted)
            else:
                encrypted_message += char
        return encrypted_message

    print('''
                             WELCOME TO THE ENCRYPTION PROGRAM

                    The purpose of this program is to encrypt a message for you.
                    The encryption process is done using Caesar Cipher.
                    Caesar cipher, in the simplest form, is shifting each 
                    character to the next one.
    ''')
    shifting = 0
    while shifting == 0:
        shifting = int(input("How many letters would you like to shift: "))

    message = input("Enter the message you wish to encrypt: \n")

    print("\nYour Encrypted Message is:")
    print(encrypt_message(message, shifting))






def check_list_program():
    def check_same_elements(list1, list2):
        return sorted(list1) == sorted(list2)

    def play_again():
        while True:
            play = input("Do you want to check another list? (yes/no): ").lower()
            if play == 'yes':
                return True
            elif play == 'no':
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    print("\n                           WELCOME TO CHECK LIST PROGRAM")
    print("                     This Program checks if the Entered lists are equal.\n")

    while True:
        list1 = input("\nEnter elements of list 1 separated by space:").split()
        list2 = input("Enter elements of list 2 separated by space:").split()

        if check_same_elements(list1, list2):
            print("The lists have the same elements. ✅\n")
        else:
            print("The lists do not have the same elements. ❌\n")

        if not play_again():
            print("Thank you for playing 🌟\n")
            break




def factorizer_program():
    def factorizer(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors

    print("\n                          WELCOME TO THE FACTORIZER PROGRAM")
    print("   This program is designed to help you quickly find all the factors of a positive integer.\n")

    while True:
        try:
            integer_num = int(input("\nEnter the positive integer you want to factorize: "))
            if integer_num < 0:
                print("Oh! You entered a negative number. Please enter a positive integer.")
                continue
            elif integer_num == 0:
                print("Zero has no factors. Please enter a positive integer.")
                continue
            else:
                factors = factorizer(integer_num)
                print("Factors of", integer_num, "are:", factors)
        except ValueError:
            print("This is an invalid input. Please enter a positive integer.")
            continue

        while True:
            continuity = input("\nDo you want to favtorize another number? (yes/no): ").lower()
            if continuity == 'no':
                print("\nThank you for using the Factorizer Program! hope it was helpful in exploring factors effortlessly🌟.")
                return
            elif continuity == 'yes':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")





def menu():
    while True:
        print()
        print("                    Hello, Let's explore some useful and joyful programs")
        print("                    ----------------------------------------------------\n")
        print("                             1. Grades Calculator Program")
        print("                             2. Armstrong Number Program")
        print("                             3. Approximations of π Program")
        print("                             4. Encryption Program")
        print("                             5. Check List Program")
        print("                             6. Factorizer Program")
        print("                             7. Exiting the menu")

        choice = input("\n                          Choose the program you want to run: ")

        if choice == '1':
            grades_calculator_program()
            return
        elif choice == '2':
            armstrong_number_program()
            return
        elif choice == '3':
            pie_calculate_program()
            return
        elif choice == '4':
            encryption_program()
            return
        elif choice == '5':
            check_list_program()
            return
        elif choice == '6':
            factorizer_program()
            return
        elif choice == '7':
            print("\n                           THANK YOU FOR USING OUR PROGRAM🌟\n")
            return False
        else:
            print("\nInvalid choice. Please choose a number between 1 and 7.")
            

def main():
    while True:
        menu()
        run_again = input("\n                          Do you want to run another program? (yes/no):").lower()
        if run_again == 'no':
            print("\n Thank you for using our program! Hope you enjoyed the trial and was satisfied.")
            return False
        elif run_again != 'yes':
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
