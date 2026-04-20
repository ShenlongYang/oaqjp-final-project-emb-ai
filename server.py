from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotionDetector():
    """Emotion detection route for the web app (matches required decorator)."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_output = (
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)