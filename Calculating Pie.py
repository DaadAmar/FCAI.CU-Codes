# File: Calculating Pie
# Purpose: A Python program that approximates 
#          the value of π (pi) using the Leibniz 
#          series formula.
# Author: Daad Amar Osman 
# Date : Feb 25, 2024
# Version : 2.0

# Initialize pie with the first term of the Leibniz series
pie = 1
terms = 0
# Initialize the counter for the loop
i = 2
print('''
                      Approximates of π   
                      
      This program will approximate the value of π using the 
      Leibniz series formula.The formula for the Leibniz series is:
      
              π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
      ''')
while terms <= 0:
    terms = int(input("Please enter the number of terms for the approximation : "))

# Check if the user entered 1, as we can directly calculate π with one term
if terms == 1:
   # Multiply by 4 as per the formula to get the approximation of π 
    pie = pie * 4
    print(f"\nThe Approximate value of π with {terms} terms is : {pie}")

# If the user entered a number greater than 1, we calculate the approximation using a loop
else:
    while i <= terms:
        # Update the approximation of π using the Leibniz series formula
        pie = pie + ((-1) ** (i + 1)) * (1 / (i + 1))
        i += 1

    # Multiply the result by 4 as per the formula to get the approximation of π
    pie = pie * 4
    
    print(f"\nThe Approximate value of π with {terms} terms is : {pie}")
