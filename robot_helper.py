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
		distance_moved = math.sqrt(a*a+b*b)
		print int(distance_moved)
		
		
robot1 = RobotHelper()
robot1.forward(5)
robot1.backward(3)
robot1.left(3)
robot1.right(2)
robot1.distance()
	
	
		
