"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor

def motor (right, left):
    leftMotor.setVelocity(left)
    rightMotor.setVelocity(right)

from controller import Robot

MAX_SPEED = 6.28
BASE_SPEED = 0.4 * MAX_SPEED

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

#leftMotor.setPosition(10.0)
#rightMotor.setPosition(10.0)

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# # set up the motor speeds at 10% of the MAX_SPEED.
# leftMotor.setVelocity(1 * MAX_SPEED)
# rightMotor.setVelocity(1 * MAX_SPEED)

gs = []
gsNames = ['gs0', 'gs1', 'gs2']
for i in range(3):
    gs.append(robot.getDevice(gsNames[i]))
    gs[i].enable(timestep)


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    gsValues = []
    for i in range(3):
        gsValues.append(gs[i].getValue())
    
    line_right = gsValues[0]
    line_center = gsValues[1]
    line_left = gsValues[2]
    
    if line_center < 350: e = 0
    elif line_right < 350: e = 1
    elif line_left < 350: e = -1
    
    kp = 50
    u = kp * e
    print(BASE_SPEED + u , BASE_SPEED - u)
    motor(BASE_SPEED + u , BASE_SPEED - u)
# Enter here exit cleanup code.