import requests # requests module for HTTP requests

# typing module for type hints
from ..typing import Model, Response, Address, Url

from .pointers.pointer_handler import from_address

from .headers.default_headers import get_default_headers

from json import loads, dumps # loads function to load json

# API class to handle requests to the OpenAI API
class Api(object):

    # initialize the class
    def __init__(self, URL: Url | str, model: Model | str) -> None: 

        """API class to handle requests to the OpenAI API"""

        self.URL = URL
        self.model = model
        self.headers = get_default_headers()

    def get_models(self) -> Model | str:

        """Get the set model"""
        return {"data": [
            {"id": "gpt-3.5-turbo"},
            {"id": "gpt-4"},
        ]}

    def chat(self, frequency_penalty: float, messages: Address, presence_penalty: float, temperature: float = 0.8, top_p: int = 1, codec: str = 'utf-8') -> Response | None:

        # write a long docstring
        """Chat with the OpenAI API and return the response as a generator object. The generator yields the response line by line. The response is decoded using the utf-8 encoding by default. The decoding can be changed by passing a different encoding to the decoding parameter."""

        # create the data
        data = {
            'frequency_penalty': frequency_penalty,
            'messages': from_address(messages),
            'model': self.model,
            'presence_penalty': presence_penalty,
            'stream': True,
            'temperature': temperature,
            'top_p': top_p,
        }

        # send the request
        response = requests.post(self.URL, headers=self.headers, json=data)

        # raise an exception if the status code is not 200
        response.raise_for_status()

        # iterate over the response
        for line in response.iter_lines():

            # check if the line is not an empty byte string
            if line != b'':

                # return the line
                yield line # Note: The return type is already in suitable OpenAI streamed format

                
    def no_stream(self, frequency_penalty: float, messages: Address, presence_penalty: float, temperature: float = 0.8, top_p: int = 1, codec: str = 'utf-8') -> str:

        # compile data
        data = {
            'frequency_penalty': frequency_penalty,
            'messages': from_address(messages),
            'model': self.model,
            'presence_penalty': presence_penalty,
            'stream': False,
            'temperature': temperature,
            'top_p': top_p,
        }

        # send the request
        response = requests.post(self.URL, headers=self.headers, json=data)

        # raise an exception if the status code is not 200
        response.raise_for_status()

        # return decoded content
        return loads(response.content.decode(codec))["choices"][0]["message"]["content"]

# Path: assets/scripts/api.py