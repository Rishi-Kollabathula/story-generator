# Story Generator

A Streamlit web app that turns a short text prompt into a 3-act story (under 500 words) using Google's Gemini API.

## Features

- Enter any topic and generate a 3-act story with one click
- Clear the response and try a new prompt
- Automatic retry when the model is temporarily busy (503 errors)
- Friendly messages for rate limits and API errors

## Tech Stack

Python, Streamlit, Gemini API (REST via `requests`), python-dotenv

## Getting Started

### Prerequisites

- Python 3.9 or newer
- A Gemini API key from [Google AI Studio](https://aistudio.google.com)

### Installation

```bash
git clone https://github.com/Rishi-Kollabathula/story-generator.git
cd story-generator
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac / Linux
python -m pip install -r requirements.txt
```

### Configuration

Create a file named `.env` in the project folder and add your key:

```
GEMINI_API_KEY=your_actual_api_key
```

Never commit your `.env` file. It is listed in `.gitignore`.

### Run the app

```bash
python -m streamlit run app.py
```

Open http://localhost:8501 in your browser.

## How It Works

1. The user enters a topic in the text box.
2. The app sends a prompt to the Gemini API: "Create a 3 act story of less than 500 words about ...".
3. The generated story is shown on the page and kept in Streamlit session state until cleared.

The app calls the Gemini REST endpoint with `requests` instead of the gRPC-based SDK, so it also runs on machines that block gRPC binaries.

## Acknowledgments

Google Gemini API, Streamlit, python-dotenv
