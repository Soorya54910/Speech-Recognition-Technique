from speech_translator import recognize_speech_from_mic, translate_text, speak_text

def main():
    print("🎤 Speech Translator - Start")
    
    # Source language (speech input) and target language (translation + speech output)
    src_language = "en-US"      # English (United States)
    target_language = "es"      # Spanish

    # Step 1: Recognize speech
    original_text = recognize_speech_from_mic(language=src_language)

    # Step 2: Translate recognized speech
    if original_text:
        translated_text = translate_text(original_text, dest_language=target_language)

        # Step 3: Speak out translated text
        speak_text(translated_text, lang=target_language)

if __name__ == "__main__":
    main()
