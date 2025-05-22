import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import tempfile
import playsound

def recognize_speech_from_mic(language="en-US"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎤 Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing speech...")
        text = recognizer.recognize_google(audio, language=language)
        print(f"📝 You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError:
        print("⚠️ Could not request results from Google Speech Recognition service")
    
    return None

def translate_text(text, dest_language="es"):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    print(f"🌍 Translated to [{dest_language}]: {translation.text}")
    return translation.text

def speak_text(text, lang="es"):
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
        tts.save(fp.name)
        playsound.playsound(fp.name)

def main():
    print("🔁 Speech Translator")
    src_language = "en-US"  # English (US)
    target_language = "es"  # Spanish

    original_text = recognize_speech_from_mic(language=src_language)
    if original_text:
        translated_text = translate_text(original_text, dest_language=target_language)
        speak_text(translated_text, lang=target_language)

if __name__ == "__main__":
    main()
