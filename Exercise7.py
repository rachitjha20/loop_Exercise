<<<<<<< HEAD
# Exercise 7: Print the following pattern
# Write a program to use for loop to print the following reverse number pattern

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1


for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
        i -= 1
=======
# Exercise 7: Print the following pattern
# Write a program to use for loop to print the following reverse number pattern

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1


for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
        i -= 1
>>>>>>> 195867aba172f01d1e354c8350f72af4c296dafe
    print()