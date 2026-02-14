# Import the requests and json libraries
import requests, json

def emotion_detector(text_to_analyze):
    '''
    Emotion detector that uses Watson NLP EmotionPredict
    input: text_to_analyze (str for emotion detection)
    output: EmotionPredict analysis of text_to_analyze (as dict)
    '''
    # Make the request to the emotionPredict API
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    # Create output for blank input entries
    if response.status_code == 400 or response.status_code == 500:
        blank_emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return blank_emotions
    # Convert text from response to json
    formatted_response = json.loads(response.text)
    # Extract the dict with emotion scores from the text output
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    # Find the emotion key with the highest score
    dominant_emotion = max(emotions, key=emotions.get)
    # Add dominant emotion to emotions dict
    emotions['dominant_emotion'] = dominant_emotion
    # Return the resulting dict
    return emotions