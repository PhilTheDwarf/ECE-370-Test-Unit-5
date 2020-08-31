from robot_control_class import RobotControl
import time

class MoveRobot:
    def __init__(self, motion, clockwise, speed, time):
        self.RC = RobotControl()
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        self.time_turn = 7.0

    def move_straight(self):
        self.RC.move_straight_time(self.motion, self.speed, self.time_turn)
    
    def turn(self):
        self.RC.turn(self.clockwise, self.speed, self.time_turn)

    def do_square(self):
        i = 0
        while (i < 4):
            self.move_straight()
            self.turn()
            i = i + 1

t1 = MoveRobot('forward', 'clockwise', 0.3, 4)
t2 = MoveRobot('forward', 'clockwise', 0.3, 8)

print("Running T1")
t1.do_square()
print("Running T2")
t2.do_square()