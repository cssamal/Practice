import math

class RobotHelper():
	
	def __init__(self, x=0.00, y=0.00):
		#initialize robot position with x,y co-ordinates with (0,0)
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
		distance_moved = math.sqrt(a*a+b*b)
		print('Distance moved by robot:{:d}'.format(int(distance_moved)))
		#Re-position robot location to (0,0)
		self.x = 0.00
		self.y = 0.00

	
	
	
		
