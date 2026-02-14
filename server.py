from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask(__name__)

@app.route("/emotionDetector", methods=['GET', 'POST'])
def emo_detector():
    '''
    Receives input text from the HTML interface (textToAnalyze).
    Outputs a string containing emotion detection analysis (responseText).
    '''
    # Get text for analysis from HTML form
    text_to_analyze = request.args.get('textToAnalyze')
    # Get output from emotion_detector 
    emotions_dict = emotion_detector(text_to_analyze)
    # Provide output for improper entries 
    if emotions_dict['dominant_emotion'] == None:
        return "<b>Invalid text! Please try again!</b>"
    # Return the required statement incorporating the results
    return (
        f"For the given statement, the system response is "
        f"'anger': {emotions_dict['anger']}, "
        f"'disgust': {emotions_dict['disgust']}, "
        f"'fear': {emotions_dict['fear']}, "
        f"'joy': {emotions_dict['joy']}, "
        f"'sadness': {emotions_dict['sadness']}. "
        f"The dominant emotion is <b>{emotions_dict['dominant_emotion']}</b>."
    )

@app.route("/")
def render_index_page():
    '''
    Renders the main application page over the Flask channel.
    '''
    return render_template("index.html")

# Allow app to be executed on localhost:5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000) 