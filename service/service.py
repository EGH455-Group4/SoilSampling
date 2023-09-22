'''Service.py holds the service level functionality of the Soil sampling app.'''
from datetime import datetime, timedelta
import time
import logging
from threading import Thread, Lock

from motor.motor import Motor
from models.constants import STARTED_SAMPLING, ALREADY_SAMPLING

class Service():
    '''Service will have service level functions.'''
    def __init__(
            self, motor: Motor
        ):
        self.motor = motor

        self.lock = Lock()

        logging.info("Service was setup")

    def start_sampling(self):
        if self.lock.locked():
            return ALREADY_SAMPLING

        self.lock.acquire()

        motor_thread = Thread(target=self.motor.sample, args=[self.lock])

        motor_thread.start()

        return STARTED_SAMPLING
