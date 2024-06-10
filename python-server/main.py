from flask import Flask, request, jsonify
import speech_recognition as sr
from pydub import AudioSegment
import io
import os
import requests
from urllib.parse import urlparse, parse_qs
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/convert', methods=['GET'])
def convert_voice_to_text():
    # Parse the URL
    parsed_url = urlparse(request.url)
    # Extract the query parameters
    query_params = parse_qs(parsed_url.query)
    # Get the 'weblink' parameter
    weblink = query_params.get('weblink', [None])[0]

    if weblink:
        try:
            # Download the .oga file
            response = requests.get(weblink)
            if response.status_code == 200:
                # Save the file locally
                with open('voice_message.oga', 'wb') as f:
                    f.write(response.content)

                # Load the audio file
                audio = AudioSegment.from_file('voice_message.oga')

                # Export the audio to WAV format in memory
                wav_io = io.BytesIO()
                audio.export(wav_io, format="wav")
                wav_io.seek(0)

                # Use SpeechRecognition to process the WAV audio
                recognizer = sr.Recognizer()
                with sr.AudioFile(wav_io) as source:
                    audio_record = recognizer.record(source)

                # Recognize speech using Google Web Speech API
                try:
                    text = recognizer.recognize_google(audio_record)
                    return jsonify({'state': True, 'text': text})
                except sr.UnknownValueError:
                    logging.error("Could not understand the audio")
                    return jsonify({'state': False, 'text': 'Could not understand the audio'}), 400
                except sr.RequestError as e:
                    logging.error(f"Google Web Speech API error: {str(e)}")
                    return jsonify({'state': False, 'text': str(e)}), 501
                finally:
                    # Delete the downloaded file
                    os.remove('voice_message.oga')
            else:
                logging.error("Failed to download the file")
                return jsonify({'state': False, 'text': 'Failed to download the file'}), 502
        except Exception as e:
            logging.error(f"Error processing voice file: {str(e)}", exc_info=True)
            return jsonify({'state': False, 'text': f'Error processing voice file: {str(e)}'}), 503
    else:
        logging.error("No weblink found in request")
        return jsonify({'state': False, 'text': 'No weblink found'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3008, debug=True)
