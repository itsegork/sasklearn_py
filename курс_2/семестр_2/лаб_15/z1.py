import math

def S(r):
  return math.pi * r*2

def l(r):

  return 2 * math.pi * r

def krug():
  r = float(input("Введите радиус окружности: "))
  print(f"Площадь круга: {S(r):.2f} Длина окружности: {l(r):.2f}")

krug()