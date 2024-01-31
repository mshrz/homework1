x = 1
n = 2
a = 25
while True:
    y = x ** n
    if y == a:
        break
    x = (x * n / y) ** (1 / (n - 1))
print(x)