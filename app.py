import math

def area_of_circle_inscribed(a, b, c, A, B, C):
  p = (a + b + c) / 2
  A = math.radians(A)
  B = math.radians(B)
  C = math.radians(C)
  R = (p - a) * math.tan(A / 2)
  return math.pi * (R**2)


a = 3
b = 4
c = 5
A = 60
B = 70
C = 80

result = area_of_circle_inscribed(a, b, c, A, B, C)
print(result)