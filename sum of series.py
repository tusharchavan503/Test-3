# sum of following series  1/1! + 2/2! + 3/3! + 4/4! + ... N/N!
n = int(input("Enter the number: "))
fact = 1
ad = 0
for i in range(1, n + 1):
    fact *= i
    summ = i / fact
    ad += summ
print(ad)
