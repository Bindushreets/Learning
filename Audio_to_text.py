import speech_recognition as sr
recogniser = sr.Recognizer()
audio_file = "Doresaani.wav"

# from pydub import AudioSegment
# AudioSegment.from_file(audio_file).export("converted.wav", format="wav")

with sr.AudioFile(audio_file) as source:
    audio_data = recogniser.record(source, duration=120)  # Adjust duration as needed

    try:
        text = recogniser.recognize_google(audio_data)
        print("Transcription:", text)

    except sr.UnknownValueError:
        print("Could not understand the audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service;", e)

'''
    Output :
            Transcription: Sada Sidha gandu Haida Ninna nodide Kannada song
'''