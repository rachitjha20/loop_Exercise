# Exercise 14: Reverse a given integer number
# Given:

# 76542

# Expected output:

# 24567


x = int(input("Enter the number: "))

rev = 0

while x > 0:
    rem = x % 10
    rev = rev*10 + rem
    x = x // 10

print (rev)
    