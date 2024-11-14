# cuddly-fortnight
An AI-powered, real-time text prediction dashboard that allows users to input text and receive predictions from a model hosted on Hugging Face. This project integrates a frontend dashboard with a Flask backend API, dynamically updating the UI with model predictions to enhance user engagement and interactivity.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Running the Application Locally](#running-the-application-locally)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your_username/your_project.git
   cd your_project
   ```

2. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) If `gunicorn` is not in your requirements, install it:

   ```bash
   pip install gunicorn
   ```

## Setup

1. Ensure your Flask application is in a file named `app.py`. The Flask app instance should be named `app` (i.e., `app = Flask(__name__)`).
   
2. Create a `Procfile` in the root directory with the following contents:

   ```
   web: gunicorn app:app
   ```

   This tells your deployment platform to use `gunicorn` to run your Flask app.

3. Ensure you have a `requirements.txt` file with all necessary dependencies, including `Flask`, `gunicorn`, and any other packages your project requires (e.g., for AI model dependencies).

   Example:

   ```
   Flask==2.1.1
   gunicorn==20.1.0
   pandas==1.4.2
   scikit-learn==1.0.2
   numpy==1.21.2
   ```

## Running the Application Locally

To run the application locally, you can use `Flask` or `gunicorn`.

### Using Flask

Run the app in development mode:

```bash
python app.py
```

### Using Gunicorn

For production-like testing, you can run the app using `gunicorn`:

```bash
gunicorn app:app
```

By default, the app will run on `http://127.0.0.1:5000/`.

## Deployment

To deploy the app to platforms like Render, follow these steps:

1. Push your repository to a remote GitHub repository (if not already done).

2. Sign in to [Render](https://render.com) or your preferred cloud platform.

3. Create a new web service and link it to your GitHub repository.

4. Render (or your platform) will automatically detect the `Procfile` and use `gunicorn` to run the Flask app.

   - Ensure that all environment variables and secrets are properly configured if required (e.g., model paths, API keys).

5. Once deployed, Render will give you a URL where your application will be accessible.

## Project Structure

Your project should have the following structure:

```
project_root/
├── app.py                    # Main Flask app file
├── Procfile                  # Specifies the app entry point for deployment
├── templates/
│   └── index.html            # HTML file for the dashboard
├── static/
│   ├── css/
│   │   └── styles.css        # CSS for styling the frontend
│   └── js/
│       └── script.js         # JavaScript for handling prediction requests and UI updates
└── requirements.txt          # List of dependencies
```

### app.py

This is where the main Flask application is defined, including routes for the web interface and any logic for handling requests (such as AI model predictions).

### Procfile

This file is required for deployment platforms like Render. It tells the platform how to run your app using `gunicorn`.

### templates/

This folder contains the HTML files used for rendering the frontend of your app.

### static/

This folder contains static files like CSS and JavaScript used for the frontend.

### requirements.txt

This file lists all the dependencies for your project, which are installed when deploying or setting up the app locally.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
