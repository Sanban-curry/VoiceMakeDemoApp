import streamlit as st

import synthezise_voice


def View():
    st.title('音声出力アプリ')

    st.markdown('### データ準備')

    input_option = st.selectbox(
        '入力データの選択',
        ('直接入力','テキストファイル')
    )


    input_data = None

    if input_option == '直接入力':
        input_data = st.text_area('こちらにテキストを入力してください。', 'Cloud Speech-to-Text用のサンプル文になります。')

    else:
        uploaded_file = st.file_uploader('テキストファイルをアップロードしてください。', ['txt'])
        if uploaded_file is not None:
            content = uploaded_file.read()
            input_data = content.decode()

    if input_data is not None:
        st.write('入力データ')
        st.write(input_data)
        st.markdown('### パラメータ設定')
        st.subheader('言語と話者の性別選択')

        lang = st.selectbox(
            '言語を選択してください',
            ('Japanese', 'English')
        )
        gender = st.selectbox(
            '話者の性別を選択してください',
            ('default', 'male', 'female', 'neutral')
        )

        st.markdown('### 音声合成')
        st.write('こちらの文章で音声を作成しますか？')
        if st.button('開始'):
            comment = st.empty()
            comment.write('音声出力を開始します。')
            responce = synthezise_voice.synthesize_speech(input_data, lang=lang, gender=gender)
            st.audio(responce.audio_content)
            comment.write('完了しました。')