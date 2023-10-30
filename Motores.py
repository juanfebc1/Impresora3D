from time import sleep
import RPi.GPIO as GPIO

DIR=20
STEP=21
CW=1
CCW=0
SPR=48

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.ouput(DIR, CW)

MODE=(14,15,18)
GPIO.setup(MODE, GPIO.OUT)

RESOLUTION = {'FULL':(0,0,0),
              'HALL':(1,0,0),
              '1/4':(0,1,0),
              '1/8':(1,1,0),
              '1/16':(0,0,1),
              '1/32':(1,0,1)}
GPIO.ouput(MODE, RESOLUTION['1/32'])

step_count=32
delay= .0208/32

for x in range(step_count):
    GPIO.ouput(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.ouput(STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.ouput(DIR, CCW)

for x in range(step_count):
    GPIO.ouput(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.ouput(STEP, GPIO.LOW)
    sleep(delay)

GPIO.cleanup()
