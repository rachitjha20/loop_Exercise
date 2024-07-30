# Exercise 5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
# Given:

# numbers = [12, 75, 150, 180, 145, 525, 50]

n = int(input("Enter the list length: "))

list1 = []

# Appending numbers in list list1
for i in range(n):
    ele = int(input(f"Enter the element at place{i}: "))
    list1.append(ele)

print()    
print(list1)

# Now using list1 as base to follow the preset conditions.
list2 = []
for i in list1:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i%5 == 0:
        print(i)