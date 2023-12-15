import pyttsx3  # Import the pyttsx3 library, which is used for text-to-speech conversion

def speak(text):
    """
    Converts the given text into speech.

    Args:
    text (str): The text to be spoken.
    """
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Get and set properties for the speech engine
    voices = engine.getProperty("voices")  # Retrieve available voices
    engine.setProperty("rate", 150)  # Set the speech rate (speed of speech)
    engine.setProperty("volume", 1)  # Set the volume (0.0 to 1.0)
    engine.setProperty("voice", voices[0].id)  # Choose the first voice in the list of voices

    # Add the text to be spoken to the engine's queue
    engine.say(text)

    # Process the speech queue; this will play the speech
    engine.runAndWait()

# This block is executed when the script is run directly (not imported as a module)
# if __name__ == "__main__":
#     # Call the speak function with a sample text
#     speak("Hello, my name is Wallace")
