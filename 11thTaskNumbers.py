x = 1 #int
y = 2.8 #float
z = 1j #complex

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 356198491611
z = -51681613

print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# float can also be scientific numbers
# with an "e" to indicate the power of 10

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1 #int
y = 2.8 #float
z = 1j #complex

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
county = 0

while county < 10:
    print(random.randrange(1,10))
    county = county + 1


