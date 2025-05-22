from utils.voice_input import get_voice_command
from controllers.appliance_controller import control_appliance

def main():
    while True:
        command = get_voice_command()
        if command:
            control_appliance(command)
            if "exit" in command or "quit" in command:
                print("Exiting program.")
                break

if __name__ == "__main__":
    main()
