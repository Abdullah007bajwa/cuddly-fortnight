from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "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")
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        user_input = request.json.get("input")
        if not user_input or not isinstance(user_input, str):
            return jsonify({'error': 'Invalid input. Please provide a valid string.'}), 400

        payload = {"inputs": user_input}
        response = requests.post(HUGGINGFACE_API_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            if isinstance(response_data, list) and "generated_text" in response_data[0]:
                prediction = response_data[0]["generated_text"]
                return jsonify({'prediction': prediction})
            else:
                return jsonify({'error': 'Unexpected response format from Hugging Face API.'}), 500
        else:
            error_message = response.json().get("error", "Unknown error")
            return jsonify({'error': f'Hugging Face API error: {error_message}'}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Network error: {str(e)}'}), 503
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
