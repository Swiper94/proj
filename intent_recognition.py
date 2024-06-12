import os
import google.cloud.dialogflow_v2 as dialogflow


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text, response.query_result.intent.display_name


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Lenovo/Desktop/ui/api_key/delta-essence-425710-p3-c59b7d3be143.json"