"""
Emotion Detection Server
This script initiates a Flask server for emotion detection analysis.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the text passed in the request arguments and returns the
    emotion scores and the dominant emotion.
    """

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Check for blank input before calling emotion_detector
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    # Pass the text to the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion
    dominant_emotion = response["dominant_emotion"]

    # Handle invalid API response
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return formatted output
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
