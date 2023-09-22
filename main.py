'''main.py is the main entrypoint to the Air Quality application.'''
from config.config import Config
from config.log import setup_logging
from service.service import Service
from handler.handler import Handler

from motor.hardware_motor import HardwareMotor
from motor.mock_motor import MockMotor

def main():
    '''Is the main start of the application.'''
    config = Config("config.json")

    setup_logging(config.get_key("log_to_file"))

    if config.get_key("mock_hardware"):
        motor = MockMotor()
    else:
        motor = HardwareMotor()

    service = Service(motor)

    handler = Handler(config, service)
    handler.Run()

if __name__ == "__main__":
    main()
