def control_appliance(command):
    if "light" in command and "on" in command:
        print("Turning on the light...")
    elif "light" in command and "off" in command:
        print("Turning off the light...")
    elif "fan" in command and "on" in command:
        print("Turning on the fan...")
    elif "fan" in command and "off" in command:
        print("Turning off the fan...")
    else:
        print("Command not recognized.")

