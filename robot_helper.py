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
		print('Distance moved by robot helper:{:d}'.format(int(distance_moved)))
		#Re-position robot location to (0,0)
		self.x = 0.00
		self.y = 0.00

def main():
	'''
	This script would move Robot Helper and provide distance moved.

	Provide movement commands as such;
	F = Forward
	B = Backward
	L = Left
	R = Right
	D = Distance

	'''
	direction = 0
	steps = 0
	command = (direction, steps)
	command_list = []
	while direction is not 'D':
		direction = input("Direction (F, B, L, R, D):")
		if direction == 'D':
			break
		steps = input("Number of steps to move:")
		command = (direction, steps)
		command_list.append(command)

	while len(command_list) > 0:
		current = command_list[-1]
		if current[0] == 'F':
			rh.forward(current[1])
		elif current[0] == 'B':
			rh.backward(current[1])
		elif current[0] == 'L':
			rh.left(current[1])
		elif current[0] == 'R':
			rh.right(current[1])
		command_list.pop()
	rh.distance()

if __name__ == '__main__':
	rh = RobotHelper()
	main()
