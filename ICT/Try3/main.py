#!/usr/bin/env pybricks-micropython 

# Importerar Pybricks Funktioner

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# If - Satser för om roboten är på banan och om den har hittat banan
on_track = False
found_track = False

# Importerar höger och vänster motor till två olika objekt, Portsen representeras av porten på roboten
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Importerar höger och vänster sensor till två olika objekt, Portsen representeras av portsen på roboten
right_sensor = ColorSensor(Port.S1)
left_sensor = ColorSensor(Port.S4)

# Importerar roboten till ett objekt och anger vilka motorer som tillhör roboten samt hjul diamter och axel längden i mm
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=118)

# Två konstater för spåret respektive underlaget som roboten kör på samt genomsnittet av de två för att roboten ska hålla sig på kanten.
LOW_REFLECTION = 3
HIGH_REFLECTION = 34
threshold = (LOW_REFLECTION + HIGH_REFLECTION)/2

# Konstant för hastigheten på roboten
DRIVE_SPEED = 25

# While loop som körs om roboten inte är på banan
while on_track == False:
    # turn_rate till noll så att roboten kör rakt fram när den letar efter bana
    turn_rate = 0

    # Roboten kör med DRIVE_SPEED konstanten som hastighet och turn_rate variablen som hur mycket den svänger
    robot.drive(DRIVE_SPEED, turn_rate)

    # Kollar om höger sensorn upp täcker banan om den hittar banan så ändras bool variablen found_track till true och roboten svänger 
    if right_sensor.reflection() < threshold:
        found_track = True
        turn_rate = -24
    # Om höger sensorn kommer över spåret så är roboten på banan och on_track sätts till true
    if found_track is True and right_sensor.reflection() > threshold:
        on_track = True
    
    # Likadant för vänster sensorn som för höger
    if left_sensor.reflection() < threshold:
        found_track = True
        turn_rate = 24
    if found_track is True and left_sensor.reflection() > threshold:
        on_track = True

# När roboten är på banan körs denn while loop
while on_track == True:
    # Räknar ut skillnaden mellan threshold och reflektionen från materialet under
    right_deviation = right_sensor.reflection() - threshold
    left_deviation = left_sensor.reflection() - threshold + 8 # Lägger till 8 för att sensorn generellt sätt hade en lägre reflektion

    # Kollar om reflektionen är lägre än threshold på någon av sensorerna om så är fallet så svänger roboten annars kör den rakt fram
    if left_deviation < threshold:
        turn_rate = 45
    elif right_deviation < threshold - 12:
        turn_rate = -45
    else:
        turn_rate = 0

    # Roboten kör med DRIVE_SPEED konstanten som hastighet och turn_rate variablen som hur mycket den svänger 
    robot.drive(DRIVE_SPEED, turn_rate)
