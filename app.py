# flask module to host server locally
from flask import Flask, request, jsonify, Response
from flask_cors import CORS # to allow cross-origin requests

# import the api
from assets.scripts.api import Api

# logging module for debugging
import logging

# set the logging level to debug
logging.basicConfig(level=logging.DEBUG)

# set the logging format
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')

# set the logging date format
logging.basicConfig(datefmt='%d-%b-%y %H:%M:%S')

# create logger
logger = logging.getLogger(__name__)

# create API instance
api = Api(
    URL='https://chat.3211000.xyz/api/openai/v1/chat/completions',
    model='gpt-3.5-turbo', # default model
)

# create the server
app = Flask(__name__)
CORS(app) # allow cross-origin requests

# route to chat with the API
@app.route('/chat/completions', methods=['POST'])
def chat():

    # get the request data
    data = request.get_json()

    # update the model based on the request data
    api.model = data['model']

    # log the incoming request
    logger.debug(f"A new request was sent for {api.model}\n Messages length (no pointer, including system): {len(data['messages'])}\nTemperature: {data['temperature']}\nTop P: {data['top_p']}\nFrequency Penalty: {data['frequency_penalty']}\nPresence Penalty: {data['presence_penalty']}\nStream: {data['stream']}\n")

    # this function is used to stream the response
    def stream():

        # generate the response
        for chunk in api.chat(
            frequency_penalty=data['frequency_penalty'],
            messages=id(data['messages']),
            presence_penalty=data['presence_penalty'],
            temperature=data['temperature'],
            top_p=data['top_p'],
        ):

            # yield the chunk
            yield chunk + b'\n\n'

    # check if the stream parameter is set to True
    if data['stream']:

        # return the response as a stream
        return Response(stream(), mimetype='text/event-stream')
    
    else:

        # get the response without streaming
        response_object = api.no_stream(
            frequency_penalty=data['frequency_penalty'],
            messages=id(data['messages']),
            presence_penalty=data['presence_penalty'],
            temperature=data['temperature'],
            top_p=data['top_p'],
        )

        # return the response as json and in the suitable OpenAI non-streamed format
        return jsonify({
            "object": "chat.completion",
            "model": f"{api.model}",
            "choices": [{
                "index": 0,
                "message": {
                    "content": f"{response_object}",
                    "role": "assistant",
                },
                "finish_reason": "stop",
                }
            ]
        }), 200
 

# route to retrieve the set model from the API
@app.route('/models', methods=['GET'])
def get_models():

    # return the models
    return jsonify(api.get_models()), 200

# root route. Used to test if the server works
@app.route('/')
def index():

    return 'Server is running!'

# run the server
if __name__ == '__main__':

    app.run(debug=False, host='0.0.0.0', port=5000)