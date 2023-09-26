
from flask import Flask, render_template, request

# Import the SpeechRecognition library
import speech_recognition as sr

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
     # Initialize an empty string for the transcript
    transcript=""
    
     # Check if the method of the request is POST (i.e., data is submitted)
    if request.method == 'POST':
        # Get the uploaded file from the form
        file = request.files['file']

         # Check if a file was uploaded
        if file:
            # Create a recognizer object from the SpeechRecognition library
            recognizer = sr.Recognizer()

             # Open the uploaded audio file and record its content
            with sr.AudioFile(file) as source:
                 data = recognizer.record(source)

            # Perform speech recognition on the recorded data using Google's API
            transcript = recognizer.recognize_google(data, key=None)

    # Render the 'index.html' template with the transcript variable
    return render_template('index.html', transcript=transcript)

if __name__ == '__main__':
    app.run(debug=True, threaded = True)
