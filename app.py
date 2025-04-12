# app.py
from flask import Flask, request, jsonify, render_template
import speech_recognition as sr
from command_processor import CommandProcessor

app = Flask(__name__)
command_processor = CommandProcessor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.json
    text = data.get('text', '')
    
    response = command_processor.process_command(text)
    return jsonify(response)

@app.route('/process_speech', methods=['POST'])
def process_speech():
    # Process speech file
    audio_data = request.files.get('audio')
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_data) as source:
        audio = recognizer.record(source)
        
    try:
        text = recognizer.recognize_google(audio)
        response = command_processor.process_command(text)
        return jsonify(response)
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)