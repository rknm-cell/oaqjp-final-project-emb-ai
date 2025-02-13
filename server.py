"""
server.py

This module sets up a Flask web application to detect emotions from text input.
It defines an endpoint '/emotion_detector' that processes POST requests and
returns the detected emotions or an error message for invalid input.
"""
from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotion_detector', methods=['POST'])
def detect_emotion():
    """
    Processes a POST request to detect emotions from the provided text.

    Retrieves JSON data from the request, extracts the text to analyze,
    and uses the emotion_detector function to determine the emotions.
    Returns a JSON response with the detected emotions or an error message
    if the input is invalid.
    """
    data = request.get_json()
    text_to_analyse = data.get('text', '')
    result = emotion_detector(text_to_analyse)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_message = (
        f"For the given statement, the system response is - Anger: {result['anger']}, " 
        f"Disgust: {result['disgust']}, "
        f"Fear: {result['fear']}, Joy: {result['joy']}, Sadness: {result['sadness']}. "
        f"Dominant emotion: {result['dominant_emotion']}."
    )

    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
