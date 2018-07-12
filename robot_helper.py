import math

class RobotHelper():
	
	def __init__(self, x=0.00, y=0.00):
		self.x = x
		self.y = y
	
	def forward(self, steps):
		self.x = self.x+float(steps)
	
	def backward(self, steps):
		self.x = self.x-float(steps)
	
	def left(self, steps):
		self.y = self.y-float(steps)
	
	def right(self, steps):
		self.y = self.y+float(steps)
	
	def distance(self):
		a = self.x
		b = self.y
		print a
		print b
		distance_moved = math.sqrt(a*a+b*b)
		print int(distance_moved)
		self.x = 0.00
		self.y = 0.00
	
	def position(self):
		print self.x
		print self.y 
	
	
		
