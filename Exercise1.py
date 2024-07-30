# Exercise 1: Print First 10 natural numbers using while loop
print("By for loop:   ", end=" ")
for i in range(1,11):
    print(i, end=" ")
    i += 1


print()

print("By while loop: ", end=" ")
i = 1
while i<=10:
    print( i, end=" ")
    i += 1