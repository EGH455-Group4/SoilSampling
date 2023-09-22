'''Will hold information belonging to the hardware motor.'''
import logging
import time
from threading import Lock

from motor.motor import Motor

class HardwareMotor(Motor):
    '''Implements the Motor class, and connects to hardware.'''
    def __init__(self):
        logging.info("Hardware motor setup")

    def sample(self, lock: Lock):
        '''Will just log out the call and wait.'''
        logging.info("Sampling process called")

        # TODO - Actually implement
        time.sleep(5)

        logging.info("Done sampling")

        # Always release the lock once done
        lock.release()