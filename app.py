
from flask import Flask, request, send_file, jsonify
from utils.openvoice_infer import generate_audio

app = Flask(__name__)

@app.route('/generate-audio', methods=['POST'])
def generate_audio_route():
    data = request.json
    text = data.get('text')
    client_id = data.get('client_id')
    voice_id = data.get('voice_id', 'joao_015')

    if not text or not client_id:
        return jsonify({"error": "Missing text or client_id"}), 400

    audio_path = generate_audio(text, client_id, voice_id)
    return send_file(audio_path, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
