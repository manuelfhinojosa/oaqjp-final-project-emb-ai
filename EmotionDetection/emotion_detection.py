import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(url, json=myobj, headers=header, timeout=10)

        if response.status_code == 200:
            formatted_response = response.json()
            emotions = formatted_response['emotionPredictions'][0]['emotion']

            anger_score = emotions['anger']
            disgust_score = emotions['disgust']
            fear_score = emotions['fear']
            joy_score = emotions['joy']
            sadness_score = emotions['sadness']
            dominant_emotion = max(emotions, key=emotions.get)

        else:
            anger_score = None
            disgust_score = None
            fear_score = None
            joy_score = None
            sadness_score = None
            dominant_emotion = None

    except requests.exceptions.RequestException:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }