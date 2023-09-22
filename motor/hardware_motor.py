'''Will hold information belonging to the hardware motor.'''
import logging
from threading import Lock

from time import sleep

from motor.motor import Motor
from models.constants import MOTOR_GPIO_PIN, T, SLEEP_INTERVAL

class HardwareMotor(Motor):
    '''Implements the Motor class, and connects to hardware.'''
    def __init__(self):
        from gpiozero import Servo

        self.servo = Servo(MOTOR_GPIO_PIN)

        logging.info("Hardware motor setup")

    def sample(self, lock: Lock):
        '''Will do the sampling process.'''
        logging.info("Sampling process called")

        for _ in range(T):
            self.servo.min()
            logging.info("Minimum Pos")
            sleep(SLEEP_INTERVAL)
            self.servo.mid()
            logging.info("Medium Pos")
            sleep(SLEEP_INTERVAL)
            self.servo.max()
            logging.info("Maximum Pos")
            sleep(SLEEP_INTERVAL)
        for _ in range(T):
            self.servo.max()
            logging.info("Max Pos")
            sleep(SLEEP_INTERVAL)
            self.servo.mid()
            logging.info("Mid Pos")
            sleep(SLEEP_INTERVAL)
            self.servo.min()
            logging.info("Min Pos")

        logging.info("Done sampling")

        # Always release the lock once done
        lock.release()
