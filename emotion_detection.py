# Import the requests library to enable POST request
import requests, json
from flask import jsonify

# Emotion detector function
def emotion_detector(text_to_analyze):
    '''
    Emotion detector using Watson NLP Emotion Predict
    input: text_to_analyze (str for emotion detection)
    output: Emotion Predict analysis of text_to_analyze in text form
    '''
    # Make the request to the emotionPredict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    # Convert text from response to json
    formatted_response = json.loads(response.text)
    # Extract scores for each emotion from json
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    # Put the emotion scores into a dict
    detected_emotions = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
    # Find the key with the highest score
    dominant_emotion = max(detected_emotions, key=detected_emotions.get)
    # Add dominant emotion to dict
    detected_emotions['dominant_emotion'] = dominant_emotion
    return (detected_emotions)
