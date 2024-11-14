# Cuddly Fortnight: AI-Powered Real-Time Text Prediction Dashboard

**Cuddly Fortnight** is an AI-powered, real-time text prediction dashboard that allows users to input text and receive predictions from a model hosted on Hugging Face. This project integrates a frontend dashboard with a Flask backend API, dynamically updating the UI with model predictions to enhance user engagement and interactivity.

**Live Demo**: [Cuddly Fortnight Live Demo](https://cuddly-fortnight-o8t6.onrender.com/)

---

## Table of Contents
1. [Installation](#installation)
2. [Setup](#setup)
3. [Running the Application Locally](#running-the-application-locally)
4. [Deployment](#deployment)
5. [Project Structure](#project-structure)
6. [License](#license)

---

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/your_username/cuddly-fortnight.git
cd cuddly-fortnight
```

Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

(Optional) If gunicorn is not listed in your `requirements.txt`, install it:

```bash
pip install gunicorn
```

---

## Setup

1. Ensure your Flask application is in a file named `app.py`. The Flask app instance should be named `app` (i.e., `app = Flask(__name__)`).

2. Create a `Procfile` in the root directory with the following contents:

```bash
web: gunicorn app:app
```

This tells your deployment platform to use **gunicorn** to run your Flask app.

3. Ensure you have a `requirements.txt` file with all necessary dependencies, including **Flask**, **gunicorn**, and any other packages your project requires (e.g., for AI model dependencies).

Example `requirements.txt`:

```
Flask==2.1.1
gunicorn==20.1.0
requests==2.27.1
python-dotenv==0.20.0
```

---

## Running the Application Locally

To run the application locally, you can use either **Flask** or **gunicorn**.

### Using Flask (Development Mode)
Run the app in development mode:

```bash
python app.py
```

By default, the app will run on `http://127.0.0.1:5000/`.

### Using Gunicorn (Production-Like Mode)
For production-like testing, you can run the app using **gunicorn**:

```bash
gunicorn app:app
```

---

## Deployment

To deploy the app to platforms like **Render** or others, follow these steps:

1. Push your repository to a remote **GitHub** repository (if not already done).

2. Sign in to **Render** (or your preferred cloud platform).

3. Create a new web service and link it to your GitHub repository.

Render (or your platform) will automatically detect the `Procfile` and use **gunicorn** to run the Flask app.

4. Ensure that all environment variables and secrets (like Hugging Face API keys) are properly configured.

5. Once deployed, Render will give you a URL where your application will be accessible. For example, you can access the live version at: [Cuddly Fortnight Live Demo](https://cuddly-fortnight-o8t6.onrender.com/)

---

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

### **app.py**
This is where the main Flask application is defined, including routes for the web interface and any logic for handling requests (such as AI model predictions).

### **Procfile**
This file is required for deployment platforms like Render. It tells the platform how to run your app using **gunicorn**.

### **templates/**
This folder contains the HTML files used for rendering the frontend of your app.

### **static/**
This folder contains static files like **CSS** and **JavaScript** used for the frontend.

### **requirements.txt**
This file lists all the dependencies for your project, which are installed when deploying or setting up the app locally.

---

## License

This project is licensed under the **MIT License** - see the LICENSE file for details.
