A = int(input("Введите число A: "))
n = int(input("Введите степень: "))
x = 1

while True:
    xk_1 = (1/n) * ((n-1) * x + A / x**(n-1))
    if xk_1 == x:
        break
    x = xk_1
print (xk_1)