#CMPS5P Final Review Stuffs
class Complex:
	def __init__(self, real=0, imag=0):
		self.r = real
		self.i = imag
	
	def printComplex(self):
		print(self.r,self.i)
	
	def abs(self):
		abs = (self.r**2 + self.i**2)**(1/2)
		return abs	

	def add(self, number):
		self.r = self.r + number.r
		self.i = self.i + number.i
	
	def compare(self, number):
		equal = False
		if self.r == number.r & self.i == number.i:
			equal = True
		return equal

complex1 = Complex(3,4)
complex1.printComplex()

complex2 = Complex(-3,2)
complex2.printComplex()

complex1.add(complex2)
complex1.printComplex()

areEqual = complex1.compare(complex2)
print(areEqual)


class Point:
	def __init__(self, xvalue=0, yvalue=0):
		self.x = xvalue
		self.y = yvalue

class Rectangle:
	def __init__(self, point1 = Point(), point2 = Point()):
		self.pt1 = point1
		self.pt2 = point2
		