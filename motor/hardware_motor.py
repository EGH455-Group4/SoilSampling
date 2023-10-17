'''Will hold information belonging to the hardware motor.'''
import logging
from threading import Lock

from time import sleep

from motor.motor import Motor
from models.constants import MOTOR_GPIO_PIN

class HardwareMotor(Motor):
    '''Implements the Motor class, and connects to hardware.'''
    def __init__(self):
        logging.info("Hardware motor setup")

        self.servo = None

    def sample(self, lock: Lock):
        '''Will do the sampling process.'''
        from gpiozero import Servo

        logging.info("Sampling process called")

        if self.servo is None:
            self.servo = Servo(MOTOR_GPIO_PIN)
            logging.info("Hardware motor initialised")
            self.servo.value = None

        self.servo.value = 1
        sleep(8)
        self.servo.value = -1
        sleep(10)
        self.servo.value = None
        sleep(1)

        logging.info("Done sampling")

        # Always release the lock once done
        lock.release()
