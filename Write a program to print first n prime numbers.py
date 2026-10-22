# Write a program to print first n prime numbers
n = int(input("Enter the number: "))
for num in range(2, n + 1):
    f = 0
    for i in range(1, num + 1):
        if num % i == 0:
            f += 1
    if f == 2:
        print(num)
