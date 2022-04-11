#!/usr/bin/env pybricks-micropython
# Imports
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color

import random as rnd

# Objects
ev3 = EV3Brick()

server = BluetoothMailboxServer()

mbox = TextMailbox("greeting", server)
parkedmbox = TextMailbox("is_parked", server)

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

line_sensor = ColorSensor(Port.S4)

parking_sensor = ColorSensor(Port.S1)

distance_sensor = UltrasonicSensor(Port.S3)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.6, axle_track=104)

# Constants
BLACK = 4
WHITE = 60
threshold = (BLACK + WHITE) / 2

DRIVE_SPEED = 75

PROPORTIONAL_GAIN = 3

# Connecting...
ev3.speaker.say("Booting up")
ev3.screen.clear()
ev3.screen.print("Waiting for conn...")
ev3.light.on(Color.YELLOW)
server.wait_for_connection()
ev3.screen.clear()
ev3.screen.print("Connected")
ev3.light.on(Color.GREEN)
mbox.wait()
ev3.screen.clear()
ev3.screen.print(mbox.read())
mbox.send("Hello to you...")

counter_threshold = rnd.randint(800,900)
counter = 0

looking_for_parking = False

while True:
    deviation = line_sensor.reflection() - threshold

    turn_rate = PROPORTIONAL_GAIN * deviation

    robot.drive(DRIVE_SPEED, turn_rate)
    if counter >= counter_threshold:
        ev3.screen.clear()
        ev3.screen.print("Looking for\nfor a place\nto park")
        mbox.send("park")
        looking_for_parking = True
        counter = 0

    if looking_for_parking is True:

        if parking_sensor.reflection() < threshold - 10 and parking_sensor.reflection() != 0:
            robot.straight(175)
            robot.turn(-90)
            if distance_sensor.distance() < 200:
                robot.turn(90)
            else:
                robot.straight(200)
                robot.drive(0, 0)
                ev3.light.on(Color.YELLOW)
                ev3.screen.clear()
                ev3.screen.print(mbox.read())
                if mbox.read() == "found_parking":
                    ev3.screen.print("Both Parked")
                    mbox.send("both_parked")
                    ev3.light.on(Color.RED)
                    time_to_wait = rnd.randint(1000, 7000)
                else:
                    mbox.wait()
                    ev3.screen.clear()
                    ev3.screen.print("Both Parked")
                    mbox.send("both_parked")
                    ev3.light.on(Color.RED)
                    time_to_wait = rnd.randint(1000, 7000)
                wait(time_to_wait)
                mbox.send("drive")
                ev3.light.on(Color.GREEN)
                robot.straight(-200)
                robot.turn(90)
                looking_for_parking = False
        counter = 0
        
    while distance_sensor.distance() < 170:
        if distance_sensor.distance() < 170:
            robot.drive(0,0)
            wait(10)
        else:
            robot.drive(DRIVE_SPEED / 2, 0)
            wait(10)

    counter += 1
    wait(10)
