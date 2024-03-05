# Program: Cesar Cipher Encryption
# Purpose: The purpose of this program is to encrypt a message for you.
#           The encryption proccess is done using Cesar Cipher.
#           Cesar cipher, in the simplest form, is shifting each 
#           character to the next one.
# Author: Daad Amar Osman
# Date : Feb 22, 2024
# Version : 3.0
def encryption():
    #welcome message
    print('''
                    WELCOME TO THE ENCRYPTION PROGRAM
          
          The purpose of this program is to encrypt a message for you.
          The encryption proccess is done using Cesar Cipher.
          Cesar cipher, in the simplest form, is shifting each 
          character to the next one.
          
          ''')
    shifting = 0
    while shifting == 0:
        shifting = int(input("How many letters would you like to shift: "))
        
    
    msg = input("\nEnter the message you wish to encrypt: \n")

    # Initialize variables
    encrypted_msg = ''
    char = 0

    # Loop through each character in the message
    while char < len(msg):
        # Get the ASCII value of the current character
        temp = ord(msg[char])
        
        # Check if the character is 'Z' (ASCII 90) and handle wrapping around
        if temp == 90 : 
            letter = 65    # Set the ASCII value of 'A'
            encrypt_letter = chr(letter)
            encrypted_msg = encrypted_msg + encrypt_letter
            char += 1      # Move to the next character in the message
            
        # Check if the character is 'z' (ASCII 122) and handle wrapping around
        elif temp == 122 :
            letter = 97     # Set the ASCII value of 'a'
            encrypt_letter = chr(letter)
            encrypted_msg = encrypted_msg + encrypt_letter
            char += 1     # Move to the next character in the message

        # Check if the character is not a letter and keep it unchanged    
        elif temp not in range (65,91) and temp not in range (97,123):
            letter = ord(msg[char]) 
            encrypt_letter = chr(letter)
            encrypted_msg = encrypted_msg + encrypt_letter
            char += 1    # Move to the next character in the message
            
        # Encrypt the letter using Caesar cipher
        else:
            # Shift the ASCII value of the current character by the specified amount
            letter = ord(msg[char]) + shifting
            encrypt_letter = chr(letter)
            encrypted_msg = encrypted_msg + encrypt_letter
            char += 1      # Move to the next character in the message

    print("\nYour Encrypted Message is : ") 
    print(encrypted_msg)

encryption()
