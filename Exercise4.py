# Exercise 4: Write a program to print multiplication table of a given number
# Given:

# num = 2
# Expected output is:

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

num = int(input("num = "))
for i in range(1, 11):
    print(i*num)