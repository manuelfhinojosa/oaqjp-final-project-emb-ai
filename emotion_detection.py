import requests  # Import the requests library

def emotion_detector(text_to_analyse):  # Define a function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection function
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API
    return response.text  # Return the response text