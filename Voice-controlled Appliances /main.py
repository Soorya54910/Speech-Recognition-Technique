from utils.voice_input import get_voice_command
from controllers.appliance_controller import control_appliance

def main():
    print("Voice-Controlled Appliance System Started")
    print("Say 'exit' or 'quit' to stop the program.\n")
    
    while True:
        command = get_voice_command()
        
        if command:
            if "exit" in command or "quit" in command:
                print("Exiting the program. Goodbye!")
                break
            control_appliance(command)
        else:
            print("No valid command detected. Please try again.")

if __name__ == "__main__":
    main()
