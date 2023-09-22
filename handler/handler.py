'''Handler will showcase the Soil Sampling endpoints'''
import logging
from flask import Flask
from flask_restful import Resource, Api, marshal

from config.config import Config
from service.service import Service
from models.models import GeneralResponse
from models.fields import general_response_fields

class Sample(Resource):
    '''Used to start sampling'''
    def __init__(self, **kwargs):
        self.service = kwargs['service']
        assert isinstance(self.service, Service)

    def post(self):
        '''The HTTP POST response'''
        status = self.service.start_sampling()
        return marshal(GeneralResponse(status=status), general_response_fields), \
            {'Access-Control-Allow-Origin': '*'}

class Handler():
    '''Used to create the soil sampling server'''
    def __init__(self, config: Config, service: Service):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(Sample, '/sample', resource_class_kwargs={
            'service': service
        })

        self.config = config

        logging.info("Handler was setup.")

    def Run(self):
        '''Will actually run the soil sampling server'''
        self.app.run(debug=False, port=self.config.get_key("port"), host="0.0.0.0")
