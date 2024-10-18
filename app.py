from flask import Flask, request, send_file, jsonify
import pyttsx3
import os

app = Flask(__name__)

# Initialize the TTS engine
engine = pyttsx3.init()

@app.route('/api/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Define the output file path
    audio_file = 'output.wav'

    # Generate speech and save to file
    engine.save_to_file(text, audio_file)
    engine.runAndWait()

    return send_file(audio_file, mimetype='audio/wav', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
