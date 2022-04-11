#!/usr/bin/env pybricks-micropython 

# Importerar Pybricks Funktioner

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color

ev3 = EV3Brick()
# If - Satser för om roboten är på banan och om den har hittat banan
on_track = True
found_track = False

# Importerar höger och vänster motor till två olika objekt, Portsen representeras av porten på roboten
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Importerar höger och vänster sensor till två olika objekt, Portsen representeras av portsen på roboten
right_sensor = ColorSensor(Port.S4)
left_sensor = ColorSensor(Port.S1)

# Importerar roboten till ett objekt och anger vilka motorer som tillhör roboten samt hjul diamter och axel längden i mm
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=118)

ev3.light.on(Color.RED)
ev3.speaker.set_speech_options(Language = 'sv')
ev3.speaker.say("HJÄLP MIG")
wait(5000)
ev3.light.on(Color.YELLOW)
wait(5000)
