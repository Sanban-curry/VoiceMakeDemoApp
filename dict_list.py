from google.cloud import texttospeech

gender_type = {
    'default': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
    'male': texttospeech.SsmlVoiceGender.MALE,
    'female': texttospeech.SsmlVoiceGender.FEMALE,
    'neutral': texttospeech.SsmlVoiceGender.NEUTRAL
}

lang_code = {
    'English': 'en-US',
    'Japanese': 'ja-JP'
}