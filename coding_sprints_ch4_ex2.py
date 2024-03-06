# Damian Hutchinson
# 2/26/2024

# 2) Calculate the sum of digits of a given number using a loop. The program
# should prompt the user to input a number and print the sum of its digits.

number = int(input("Please enter a number"))

total = 0

while number > 0:
    digit = number %  10
    total = total + digit
    number = number // 10

print("The sum of all digits for", number , "is =", total)
