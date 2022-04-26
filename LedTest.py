import RPi.GPIO as GPIO
from time import sleep

# Available GPIO pins are 5, 6, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27

def yellow(red, green, boolean):
    GPIO.output(red, boolean)
    GPIO.output(green, boolean)

def greenLight(green, boolean):
    GPIO.output(green, boolean)

def whiteLight(red, green, blue, boolean):
    GPIO.output(red, boolean)
    GPIO.output(green, boolean)
    GPIO.output(blue, boolean)

GPIO.setmode(GPIO.BCM)

red = [5, 6, 12, 13, 16]
green = [17, 18, 19, 20, 21]
blue = [22, 23, 24, 25, 26]

test = True

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# light test
while test:
    for i in range(len(red)):
        yellow(red[i], green[i], True)
        sleep(1)
        yellow(red[i], green[i], False)
    for i in range(len(blue)):
        greenLight(green[i], True)
        sleep(1)
        greenLight(green[i], False)
    for i in range(len(blue)):
        whiteLight(red[i], green[i], blue[i], True)
        sleep(1)
        whiteLight(red[i], green[i], blue[i], False)
    GPIO.cleanup
