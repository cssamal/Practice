#!/usr/bin/env python3

from math import sqrt


class RobotHelper:

    def __init__(self, x=0, y=0):
        # initialize robot position with x,y co-ordinates with (0,0)
        self.x = x
        self.y = y

    def forward(self, steps):
        self.x = self.x + float(steps)

    def backward(self, steps):
        self.x = self.x - float(steps)

    def left(self, steps):
        self.y = self.y - float(steps)

    def right(self, steps):
        self.y = self.y + float(steps)

    def distance(self):
        distance_moved = sqrt(self.x * self.x + self.y * self.y)
        print('Distance moved by robot helper:{:d}'.format(int(distance_moved)))

    def main(self):
        command_list = []
        while 1:
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
    rh.main()

