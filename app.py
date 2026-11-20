import os
import time
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if gemini_api_key is None:
    raise ValueError("GEMINI_API_KEY is not set in the environment.")

# If you get a 404 / "model not found" error, change this to a current model name
# from Google AI Studio.
MODEL = "gemini-3.8-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


def create_story(prompt: str) -> str:
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"Create a 3 act story of less than 500 words about {prompt}"}
                ]
            }
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": gemini_api_key,
    }

    for attempt in range(4):
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)

        if response.status_code == 503 and attempt < 3:
            time.sleep(2 * (attempt + 1))  # wait 2s, 4s, 6s, then try again
            continue

        if response.status_code != 200:
            raise RuntimeError(f"{response.status_code}: {response.text}")

        data = response.json()
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            raise RuntimeError("The API returned no story. Try a different prompt.")


def main():
    st.title("Story Generator")

    prompt = st.text_input("Create a 3 act story of less than 500 words about:")

    if st.button("Generate Story"):
        if prompt:
            try:
                with st.spinner("Writing your story..."):
                    st.session_state["story"] = create_story(prompt)
            except Exception as e:
                if "503" in str(e):
                    st.error("The model is busy right now. Please try again in a minute.")
                elif "429" in str(e) or "quota" in str(e).lower():
                    st.error("Rate limit reached (5 requests/minute on the free tier). Wait a minute and try again.")
                else:
                    st.error(f"Something went wrong: {e}")
        else:
            st.warning("Please enter a prompt.")

    if "story" in st.session_state:
        if st.button("Clear Response"):
            del st.session_state["story"]
            st.rerun()
        else:
            st.header("Generated Story:")
            st.write(st.session_state["story"])


if __name__ == "__main__":
    main()