
import os
from openvoice import OpenVoiceModel  # Exemplo fictício
from openvoice.utils import load_reference_voice

MODEL_PATH = './models'
OUTPUT_DIR = './outputs'

def generate_audio(text, client_id, voice_id):
    model_file = os.path.join(MODEL_PATH, f"{voice_id}_voice.pth")
    model = OpenVoiceModel.load(model_file)
    reference_voice = load_reference_voice(model_file)

    audio_output = model.synthesize(text, reference_voice)
    audio_path = os.path.join(OUTPUT_DIR, f"audio_{client_id}.mp3")

    with open(audio_path, 'wb') as f:
        f.write(audio_output)

    return audio_path
