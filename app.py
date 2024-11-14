from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests

# Load Hugging Face API key from environment variable for security
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "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")  # Replace 'your_default_key' for local testing
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

@app.route('/')
def home():
    """Serves the main HTML page."""
    return render_template('index.html')  # HTML file should be located in the 'templates' folder

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles prediction requests from the client.
    Expects a JSON payload with the user input: { "input": "Your query here" }
    """
    try:
        # Parse user input from the request
        user_input = request.json.get("input")
        if not user_input or not isinstance(user_input, str):
            return jsonify({'error': 'Invalid input. Please provide a valid string.'}), 400

        # Send the user input to Hugging Face API
        payload = {"inputs": user_input}
        response = requests.post(HUGGINGFACE_API_URL, headers=HEADERS, json=payload)

        # Handle API response
        if response.status_code == 200:
            # Extract and return the generated text
            response_data = response.json()
            if isinstance(response_data, list) and "generated_text" in response_data[0]:
                prediction = response_data[0]["generated_text"]
                return jsonify({'prediction': prediction})
            else:
                return jsonify({'error': 'Unexpected response format from Hugging Face API.'}), 500
        else:
            # Return error if Hugging Face API fails
            error_message = response.json().get("error", "Unknown error")
            return jsonify({'error': f'Hugging Face API error: {error_message}'}), response.status_code

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return jsonify({'error': f'Network error: {str(e)}'}), 503
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Enable debug mode for local development
    app.run(debug=True)
