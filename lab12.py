# 1. Complex Number Class
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(2, 3)
c2 = Complex(1, 4)
print("Complex Sum:", c1 + c2)
print("Complex Difference:", c1 - c2)

print("\n" + "-"*40)

# 2. Matrix Class
class Matrix:
    def __init__(self, data):
        self.data = data

    def add(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)])

    def multiply(self, other):
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        return Matrix(result)

    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(3)] for i in range(3)])

    def display(self):
        for row in self.data:
            print(row)

m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[9,8,7],[6,5,4],[3,2,1]])
print("Matrix Addition:")
m1.add(m2).display()
print("Matrix Multiplication:")
m1.multiply(m2).display()
print("Matrix Transpose:")
m1.transpose().display()

print("\n" + "-"*40)

# 3. Solid Class
class Solid:
    def __init__(self, shape, **kwargs):
        self.shape = shape
        self.data = kwargs

    def surface_area(self):
        if self.shape == "cube":
            return 6 * self.data['side']**2
        elif self.shape == "sphere":
            return 4 * 3.14 * self.data['radius']**2

    def volume(self):
        if self.shape == "cube":
            return self.data['side']**3
        elif self.shape == "sphere":
            return (4/3) * 3.14 * self.data['radius']**3

s = Solid("cube", side=3)
print("Cube Surface Area:", s.surface_area())
print("Cube Volume:", s.volume())

print("\n" + "-"*40)

# 4. Shape Class
class Shape:
    def __init__(self, shape, **kwargs):
        self.shape = shape
        self.data = kwargs

    def perimeter(self):
        if self.shape == "square":
            return 4 * self.data['side']
        elif self.shape == "circle":
            return 2 * 3.14 * self.data['radius']

    def area(self):
        if self.shape == "square":
            return self.data['side']**2
        elif self.shape == "circle":
            return 3.14 * self.data['radius']**2

sh = Shape("circle", radius=5)
print("Circle Perimeter:", sh.perimeter())
print("Circle Area:", sh.area())

print("\n" + "-"*40)

# 5. Time Class
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_minutes(self, mins):
        total = self.hours * 60 + self.minutes + mins
        self.hours = total // 60
        self.minutes = total % 60

    def __str__(self):
        return f"{self.hours}h:{self.minutes}m"

t = Time(1, 45)
t.add_minutes(80)
print("Updated Time:", t)

print("\n" + "-"*40)

# 6. Date Class with == Overload
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)

d1 = Date(24, 4, 2025)
d2 = Date(24, 4, 2025)
print("Dates are equal:", d1 == d2)

print("\n" + "-"*40)

# 7. Weather Class with 'in' Overload
class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

w = Weather(["sunny", "cloudy", "rainy"])
print("Is 'rainy' in weather?:", "rainy" in w)

print("\n" + "-"*40)

# 8. String Class with Overloaded +=, toLower, toUpper
class String:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other.value
        return self

    def toLower(self):
        return self.value.lower()

    def toUpper(self):
        return self.value.upper()

s1 = String("Hello")
s2 = String("World")
s1 += s2
print("Concatenated String:", s1.value)
print("Lowercase:", s1.toLower())
print("Uppercase:", s1.toUpper())
