import math
(1)
a = float(input("Podaj długość boku kwadratu: "))

pole = a * a

print(f"Pole kwadratu wynosi:", pole)


(2)
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
h = float(input("Podaj h: "))

P = ((a + b) * h) / 2

print("Pole trapezu wynosi:", P)


(3)
r = float(input("Podaj r: "))

P = math.pi * r ** 2

print("Pole koła wynosi:", P)


(4)
a = float(input("Podaj a: "))
h = float(input("Podaj h: "))

P = (a * h) / 2

print("Pole trójkąta wynosi:", P)


(5)
a = float(input("Podaj a: "))
h = float(input("Podaj h: "))

P = a * h

print("Pole równoległoboku wynosi:", P)