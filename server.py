"""
This module runs the backend web server for the emotion_detection application.
        
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Retrieves the text to analyze
        
    """

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is"
    f"'anger': {anger_score}, 'disgust': {disgust_score}," 
    f"'fear': {fear_score}, 'joy': {joy_score} and 'sadness'"
    f": {sadness_score}. The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    """
    Renders template
        
    """

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
