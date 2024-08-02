# Exercise 6: Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.

# For example, the number is 75869, so the output should be 5.

counter = 0

number = int(input("Enter the number"))

while number !=0:
    counter += 1
    number = number//10

print(counter)
    