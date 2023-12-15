import json, pyttsx3, speech_recognition, bin.google_calendar as google_calendar

def setup_voice():
    """Sets up the voice for the AI to use."""
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    voices = engine.getProperty("voices")  # Retrieve available voices
    index_value = 0

    # Display information about each available voice
    for voice in voices:
        print("Voice: " + str(index_value)) 
        print("ID: %s" %voice.id) 
        print("Name: %s" %voice.name) 
        print("Age: %s" %voice.age) 
        print("Gender: %s" %voice.gender) 
        print("Languages Known: %s" %voice.languages + "\n") 
        index_value += 1

    # User selects the voice index to use
    index = input("Please enter the index of the voice you would like to use (Starts with 0): ")
    voice = voices[int(index)].id
    return voice

def openai_setup():
    """Sets up the OpenAI API key and organization ID."""
    key = input("Please enter your OpenAI API key: ")
    org = input("Please enter your OpenAI organization ID: ")

    return {"key": key, "org": org}

def speech_recognition_setup():
    """Sets up the microphone for speech recognition."""
    index = 0

    # List all available microphones
    for device in speech_recognition.Microphone.list_microphone_names():
        print(str(index) + ". " + device)
        index += 1

    # User selects the microphone index to use
    selection = input("Please enter the index of the microphone you would like to use (Starts with 0): ")
    return selection

def google_calendar_setup():
    """Demonstrates fetching and displaying upcoming Google Calendar events."""
    service = google_calendar.google_authenticate()  # Authenticate with Google Calendar
    events = google_calendar.google_get_next_events(5, service)  # Get next 5 events
    for event in events:
        print(event)  # Display each event

def chatbot_setup():

    user_input = input("Please enter the url of your chatbot: e.g. 192.168.0.10 \n")
    return user_input

def main():
    """Main function for setting up various components."""
    # Load existing settings from a JSON file
    json_data = json.load(open("data/configs/settings.json"))

    # Main loop for setup options
    while True:
        selection = input("Please select which option you would like to setup: \n1. Voice\n2. OpenAI\n3. Speech Recognition\n4. Google Calendar\n5. Personal AI URL\n6. All\n7. Save and Exit\nInput: ")

        # Process user's selection for various setups

        # Voice
        if selection == "1":
            json_data["voice_id"] = setup_voice()
        # OpenAI
        elif selection == "2":
            keyandorg = openai_setup()
            json_data["openai_key"] = keyandorg["key"]
            json_data["openai_org"] = keyandorg["org"]
        # Speech Recognition
        elif selection == "3":
            json_data["microphone_index"] = speech_recognition_setup()
        # Google Calendar
        elif selection == "4":
            google_calendar_setup()
        # Pass
        elif selection == "5":
            json_data["personal_ai_url"] = chatbot_setup()
        # All
        elif selection == "6":
            # Setup all components
            json_data["voice_id"] = setup_voice()
            keyandorg = openai_setup()
            json_data["openai_key"] = keyandorg["key"]
            json_data["openai_org"] = keyandorg["org"]
            json_data["microphone_index"] = speech_recognition_setup()
            json_data["personal_ai_url"] = chatbot_setup()
            google_calendar_setup()
        # Save and Exit
        elif selection == "7":
            # Save the settings to the JSON file and exit
            json.dump(json_data, open("data/configs/settings.json", "w"))
            exit()

if __name__ == "__main__":
    main()
