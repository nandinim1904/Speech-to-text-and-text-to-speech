import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
import playsound
from googletrans import Translator

def get_language_choice(prompt):
    print(f"\n{prompt}")
    print("1. English")
    print("2. Hindi")
    print("3. Kannada")
    print("4. korean")
    print("5. Japanese")
    
    choice = input("Choose language (1-5): ")
    languages = {
        '1': ('en', 'english'),
        '2': ('hi', 'hindi'),
        '3': ('kn', 'kannada'),
        '4': ('ko', 'korean'),
        '5': ('ja', 'japanese')
    }
    return languages.get(choice, ('en', 'english'))

def speech_to_text():
    recognizer = sr.Recognizer()
    translator = Translator()
    
    # Get input and output languages
    input_lang, input_name = get_language_choice("Select INPUT language:")
    output_lang, output_name = get_language_choice("Select OUTPUT language:")
    
    with sr.Microphone() as source:
        print(f"\nListening... Speak in {input_name.upper()}!")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        
    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio, language=input_lang)
        print(f"\nYou said ({input_name}):", text)
        
        # Translate text
        translated = translator.translate(text, src=input_lang, dest=output_lang)
        print(f"Translation ({output_name}):", translated.text)
        
        # Convert translation to speech
       # tts = gTTS(text=translated.text, lang=output_lang)
        #tts.save("temp_speech.mp3")
        #playsound.playsound("temp_speech.mp3")
        #os.remove("temp_speech.mp3")
        
        return text
    except sr.UnknownValueError:
        print("Sorry, couldn't understand the speech.")
        return None
    except sr.RequestError:
        print("Service error. Check your internet connection.")
        return None
    except Exception as e:
        print(f"Translation error: {str(e)}")
        return None

def text_to_speech(text):
    input_lang, input_name = get_language_choice("Select INPUT language:")
    output_lang, output_name = get_language_choice("Select OUTPUT language:")
    
    try:
        translator = Translator()
        translated = translator.translate(text, src=input_lang, dest=output_lang)
        print(f"\nTranslation ({output_name}):", translated.text)
        
        tts = gTTS(text=translated.text, lang=output_lang)
        tts.save("temp_speech.mp3")
        playsound.playsound("temp_speech.mp3")
        os.remove("temp_speech.mp3")
    except Exception as e:
        print(f"Translation error: {str(e)}")
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def main():
    while True:
        print("\n=== Speech and Text Converter ===")
        print("1. Speech to text")
        print("2. Text to speech")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            speech_to_text()
        elif choice == '2':
            text = input("\nEnter the text to translate: ")
            text_to_speech(text)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()