'''This will hold information about an abstract class about the motor.'''
from abc import ABC, abstractmethod

from threading import Lock

class Motor(ABC):
    '''Motor is an abstract class that other classes will implement.'''

    @abstractmethod
    def sample(self, lock: Lock):
        '''Will tell the motor to start the sampling process.'''
