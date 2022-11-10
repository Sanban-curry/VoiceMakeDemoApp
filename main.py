import os

from google.cloud import texttospeech


import synthezise_voice


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'


gender = 'default'
lang = 'English'
text = "Hi, I am goodlooking genius guy.。"

def main():


    response = synthezise_voice.synthesize_speech(text, lang, gender)

    file_name = 'output.mp3'
    with open(file_name, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


if __name__ == '__main__':
    main()

