'''This file holds the models used throughout the soil sampling program.'''
class GeneralResponse:
    '''General response is the generic response object.'''
    def __init__(self, status: str):
        self.status = status
