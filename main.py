import os

from google.cloud import texttospeech


import app

gender_type = app.gender_type
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'
gender = 'default'
def main():


    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text="こんにちは、私はとってもイケメンな天才青年です。")

    voice = texttospeech.VoiceSelectionParams(
        language_code="ja-JP", ssml_gender=gender_type[gender]
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    file_name = 'output.mp3'
    with open(file_name, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


if __name__ == '__main__':
    main()

