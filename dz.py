x = int(input("Введите положительное целое число: "))
n = int(input("Введите степень: "))

xn = x 
i = 0

while i < n:
    xn -= (xn*xn - x)/(n*xn)
    i += 1

print(int(xn))