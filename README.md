# NextWeb-Wrapper

NextWeb-Wrapper is a Flask-based reverse proxy script designed to host large language models (LLMs) such as OpenAI's GPT 3.5. Acting as an intermediary, this wrapper facilitates communication with the OpenAI models, providing a streamlined interface for developers to interact with powerful language generation capabilities.

## Features

- **Versatile Hosting**: NextWeb-Wrapper serves as a versatile hosting solution for OpenAI models, including the powerful GPT 3.5 Turbo and GPT-4.
  
- **Dynamic Model Switching**: The wrapper allows dynamic switching of models based on incoming requests, enabling flexibility in choosing the appropriate model for specific tasks.

- **Streamlined API Interaction**: The script provides a simple yet powerful API for developers to integrate with OpenAI models seamlessly.

- **Cross-Origin Resource Sharing (CORS) Support**: Cross-origin requests are supported, allowing integration with applications running on different domains.

- **Real-time Streaming**: The wrapper supports real-time streaming of responses, providing a continuous flow of data for interactive applications.

## Getting Started

### Prerequisites

- Python 3.x (3.10 tested)
- Flask (``flask``)
- Flask CORS (``flask_cors``)
- Requests

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Recentaly/NextWeb-Wrapper.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Flask server:

   ```bash
   python app.py
   ```

2. Access the server at [http://localhost:5000](http://localhost:5000).

## API Endpoints

### `/chat/completions` (POST)

This endpoint handles chat requests with the OpenAI API. The request should include parameters such as model, messages, temperature, top_p, frequency_penalty, presence_penalty, and stream. Responses can be streamed in real-time or returned without streaming.

### `/models` (GET)

This endpoint retrieves the available models for use with the API.

### `/` (GET)

The root endpoint to test if the server is running.

## Code Structure

- **app.py**: The main script containing the Flask application and API routes.
  
- **assets/scripts/api.py**: Handles communication with the OpenAI API, providing methods for chatting, getting models, and managing API requests.

- **assets/scripts/headers/get_headers.py**: Defines default headers for API requests.

- **assets/scripts/pointers/pointer_handler.py**: Manages pointers and converts them to appropriate formats.

## License

This project is licensed under the [MIT License](LICENSE).

## Legal

Please refer to the [Legal Notice](LEGAL) for clarifications.

---
