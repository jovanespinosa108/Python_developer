#se cumple else
a = 3
b = 2

if a < b:
    print("A es menor que B")
elif a == b:
    print("A es igual a B")
else:
    print("A es mayor que B")

#se cumple if
c = 4
d = 6

if c < d:
    print("c es menor que d")
elif c == d:
    print("c es igual a d")
else:
    print("c es mayor que d")

# se cumple elif
e = 5
f = 5

if e < f:
    print("e es menor que f")
elif e == f:
    print("e es igual a f")
else:
    print("e es mayor que f")

#if is
g = False

if type(g) is bool:
    print("G is boolean")
else:
    print("G es otro typo de dato")

h = 10
i = 5
j = 1

if h > i and i > j:
    print("Las dos condiciones son verdaderas")

k = 20
l = 15
m = 10

if k < l or l > m:
    print("Por lo menos una de las dos condiciones se cumple")