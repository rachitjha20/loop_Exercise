# Exercise 15: Use a loop to display elements from a given list present at odd index positions
# Given:

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Note: list index always starts at 0

# Expected output:

# 20 40 60 80 100


x = []
n = int(input("Number of elements in list are(from 0 to): "))
ele = int(input("element: "))
for i in range (0, n, 1):
    ele = int(input("element: "))
    x.append(ele)
    print(x)
    
for i in x[::2]:
    
    print(i, end=" ")
     