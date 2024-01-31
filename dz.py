  
def power(a, b):
    result = 1
    while b:
        if b % 2 == 0:
            b //= 2
            a *= a
        else:
            result *= a
            b -= 1
    return result


def root(a, n):
    assert n >= 2
    if n == 2:
        return a
    else:
        b = n // 2 + 1
        c = power(a, 1 / b)
        d = root(c, n - b) + root(c, b)
        return d

a = int(input("Введите положительное целое число: "))
n = int(input("Введите степень: ")) 
print (root)(a,n)
