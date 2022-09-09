#!/usr/bin/python
# -*- coding: latin-1 -*-

from time import sleep
import RPi.GPIO as GPIO
from ast import arg
import threading

DIR1 = 20   # Direction GPIO Pin
STEP1 = 21  # Step GPIO Pin
DIR2 = 9
STEP2 = 11

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
#SPR = 800   # Steps per Revolution (360 / 7.5)
SPR1=0
SPR2=0
def start_motor(distance_cm_1, distance_cm_2):
   SPR1 = 50 * distance_cm_1
   SPR2 = 50 * distance_cm_2
   return SPR1,SPR2
   
   
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)
GPIO.output(DIR1, CW)

GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.output(DIR2, CW)
 
MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
GPIO.output(MODE, RESOLUTION['Full'])

SPR1,SPR2=start_motor(3, 5)
step_count1 = SPR1 
step_count2 = SPR2
delay = .00150

def run(motor_id):   
      
    for x in range(step_count1):
     GPIO.output(STEP1, GPIO.HIGH)
     sleep(delay)
     GPIO.output(STEP1, GPIO.LOW)
     sleep(delay)
     print(f'motor {motor_id} calismasi tamamlandi')
     # sleep(0.5) 
     
def start(motor_id2):     
    for x in range(step_count2):
     GPIO.output(STEP2, GPIO.HIGH)
     sleep(delay)
     GPIO.output(STEP2, GPIO.LOW)
     sleep(delay)
     print(f'motor {motor_id2} calismasi tamamlandi')
     

if __name__ == "__main__":


   th1 = threading.Thread(target=run, args=[1])
   th2 = threading.Thread(target=start, args=[2])

   th1.setDaemon(True)
   th2.setDaemon(True)

   th1.start()
   th2.start()
   sleep(6)
   

   print("islem tamamlandi")


th1.join()
th2.join()

GPIO.cleanup()