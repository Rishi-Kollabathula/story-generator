# Story Generator Streamlit App

This Streamlit app uses the Google Generative AI API to generate stories based on user prompts. Users can input a prompt, generate a story, and clear the response.

## Getting Started

To run the app locally, follow these steps:

### Prerequisites

Make sure you have Python 3.9 or newer and pip installed on your system.

### Installation
Clone the repository:
```bash
git clone https://github.com/Rishi-Kollabathula/story-generator.git
```

Navigate to the project directory:
```bash
cd story-generator
```

Install dependencies:
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Running the App
Run the Streamlit app:

```bash
streamlit run app.py
```

The app will be accessible in your web browser at http://localhost:8501.

### Usage
Enter a prompt in the provided text input.
Click the "Generate Story" button to generate a story based on the prompt.
The generated story will be displayed under the prompt.
Click the "Clear Response" button to clear the generated story.

### Configuration
Create a file named `.env` in the project root and add your API key:

```
GEMINI_API_KEY=your_actual_api_key
```

Replace `your_actual_api_key` with your real Gemini API key.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
Google Generative AI
Streamlit
python-dotenv

Feel free to contribute and improve the app!

vbnet


Replace `yourusername` in the repository URL with your actual GitHub username if you decide to host the code on GitHub. Adjust the content and structure as needed based on your preferences and additional information about the project.


Tutorial at [gemini](https://www.kdnuggets.com/how-to-access-and-use-gemini-api-for-free)

Learn [prompt engineering](https://arize.com/blog-course/evaluating-prompt-playground/)
