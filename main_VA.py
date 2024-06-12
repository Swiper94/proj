import speech_recognition as sr
from text_to_speech_test import speak_text
from news_browse import fetch_news
from weather_browse import get_weather_report
from intent_recognition import detect_intent_texts
from wikipedia_search import search_wikipedia  # Import the function
import uuid

def process_command(text):
    # Dialogflow project configuration
    project_id = "delta-essence-425710-p3"
    session_id = str(uuid.uuid4())
    language_code = "ne"

    # Detect the intent using Dialogflow
    intent_response, intent_name = detect_intent_texts(project_id, session_id, text, language_code)
    print(f"Intent: {intent_name}, Response: {intent_response}")

    if intent_name == "NEWS":
        news = fetch_news()
        print(news)
        speak_text(news)
        result = news
    elif intent_name == "WEATHER":
        weather_report = get_weather_report()
        print(weather_report)
        speak_text(weather_report)
        result = weather_report
    elif intent_name == "INTRODUCTION":
        print(intent_response)
        speak_text(intent_response)
        result = intent_response
    elif intent_name == "GREETING":
        print(intent_response)
        speak_text(intent_response)
        result = intent_response
    elif intent_name == "WIKI":
        wiki_response = search_wikipedia(text)
        print(wiki_response)
        speak_text(wiki_response)
        result = wiki_response
    else:
        print(intent_response)
        speak_text(intent_response)
        result = intent_response

    return result

def recognize_speech_from_text(text):
    response = {
        "success": True,
        "error": None,
        "transcription": text
    }
    return response

def main(text):
    response = recognize_speech_from_text(text)
    if response["success"]:
        final_result = process_command(response["transcription"])
    else:
        print("Error: {}".format(response["error"]))
        final_result = None
    return final_result

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        main(text)