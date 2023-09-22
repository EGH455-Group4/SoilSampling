'''Will hold information belonging to the mock motor.'''
import logging
import time
from threading import Lock

from motor.motor import Motor

class MockMotor(Motor):
    '''Implements the Motor class, and connects to mocked hardware.'''
    def __init__(self):
        logging.info("Mock motor setup")

    def sample(self, lock: Lock):
        '''Will just log out the call and wait.'''
        logging.info("Sampling process called to mock motor")

        time.sleep(5)

        logging.info("Done sampling")

        # Always release the lock once done
        lock.release()
