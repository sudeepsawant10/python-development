import speech

recognizer = Speech.recongnition.Recognizer()

with Speech_recongnition.Microphone() as Source:
    print("Say something! ")

    #Audio from user
    audio = recognizer.listen(Source)
    print("Google Speech Recognition thinks you said: ")
    print(recognizer.recognizer_google(audio))