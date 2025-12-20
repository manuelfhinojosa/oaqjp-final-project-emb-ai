import requests  # Import the requests library
import json #Import json library

def emotion_detector(text_to_analyse):  # Define a function
    if not text_to_analyse:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection function
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the request

    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API

    if response.status_code == 200:
        formatted_response = json.loads(response.text) #Formatting response
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        dominant_emotion = max(emotions, key = emotions.get)

    elif response.status_code == 500:
        dominant_emotion = None
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None        


    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion} # Return the response