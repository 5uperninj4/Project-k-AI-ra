import pyttsx3 as tts
import speech_recognition as sr
import pocketsphinx
import multiprocessing as mp

engine = tts.init() # object creation

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def speak(queue):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            try:
                text = queue.get()
                if text:
                    engine.say(text)
                    print(text)
                    engine.runAndWait()
                else:
                    break
            except Exception as e:
                print(e)
                print('Error raised in speak function')

if __name__ == "__main__":
    queue = mp.Queue()
    speaker_process = mp.Process(target=speak, args=(queue,))
    speaker_process.start()
    speaker_process.join()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Say something!")
            audio = r.listen(source)
            text = r.recognize_sphinx(audio)
            queue.put(text)
    

