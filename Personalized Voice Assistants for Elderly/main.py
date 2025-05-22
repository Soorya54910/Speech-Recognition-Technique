# main.py
from assistant.voice_input import listen
from assistant.voice_output import speak
from assistant.medication_reminder import check_medications
from assistant.emergency_module import check_emergency

def main():
    speak("Hello! I am ElderVoice, your personal assistant. How can I help you today?")
    
    while True:
        try:
            query = listen().lower()
            
            if not query:
                speak("I didn't hear anything. Could you please repeat?")
                continue

            if "medication" in query:
                check_medications()
            elif "emergency" in query or "help" in query:
                check_emergency()
            elif "exit" in query or "stop" in query:
                speak("Goodbye! Stay safe and take care.")
                break
            else:
                speak("I'm sorry, I didn't understand that. Can you try again?")
        
        except KeyboardInterrupt:
            speak("Voice assistant stopped. Goodbye!")
            break
        except Exception as e:
            speak(f"Oops, something went wrong: {str(e)}")

if __name__ == "__main__":
    main()
