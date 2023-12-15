import bin.speech as speech
import bin.text_to_speech as text_to_speech
from tkinter import *
import speech_recognition
import json

def gui_main():
    """Creates a graphical user interface (GUI) for user interaction with the chatbot."""

    def on_submit(events=None):
        """Handles the submission of user input in the GUI.
        
        Args:
        events (None): Default argument for binding to the return key."""
        print("Submitted")  # Log submission
        user_input = input_field.get()  # Get user input from the input field

        output_field.config(state='normal')  # Enable the output field for text insertion
        output_field.insert('end', 'User: ' + user_input + '\n', 'blue')  # Display user input in blue
        response = speech.speech_to_text(user_input)  # Process user input to get response
        output_field.insert('end', 'Wallace: ' + response + '\n', 'red')  # Display AI response in red

        input_field.delete(0, 'end')  # Clear the input field
        output_field.config(state='disabled')  # Disable the output field after insertion

    # Initialize the main window of the GUI
    root = Tk()
    root.title("Wallace")  # Set title of the window

    # Create a frame for output text
    output_frame = Frame(root)
    output_frame.pack(side='top', fill='both', expand=True)

    # Label and text field for the chatbot's responses
    output_label = Label(output_frame, text="Wallace:")
    output_label.pack(side='left', padx=5, pady=5)

    output_field = Text(output_frame)
    output_field.pack(side='left', fill='both', expand=True, padx=5, pady=5)
    output_field.config(state='disabled')  # Initially disabled for editing
    output_field.tag_config('blue', foreground='blue')  # Configure blue tag
    output_field.tag_config('red', foreground='red')  # Configure red tag
    output_field.config(font=("Futura", 16))  # Set font

    # Frame for user input
    input_frame = Frame(root)
    input_frame.pack(side='bottom', fill='x')

    # Label and entry field for user input
    input_label = Label(input_frame, text="User:")
    input_label.pack(side='left', padx=5, pady=5)

    input_field = Entry(input_frame, width=150)
    input_field.pack(side='left', padx=5, pady=5)
    input_field.bind("<Return>", on_submit)  # Bind return key to submit action

    # Button for submitting the input
    submit_button = Button(input_frame, text="Submit", command=on_submit)
    submit_button.pack(side='left')

    root.mainloop()  # Start the GUI event loop

def voice():
    """Enables voice control for interaction with the chatbot."""
    recognizer = speech_recognition.Recognizer()
    device_index = json.load(open("data/configs/settings.json"))["microphone_index"]  # Load microphone index

    while True:
        try:
            # Start listening with the microphone
            with speech_recognition.Microphone(device_index=int(device_index)) as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)  # Convert speech to text
                
                if "Wallace" in text or "wallace" in text:
                    print("Person: " + text)  # Log the recognized text

                response = speech.speech_to_text(text)  # Get response from speech processing
                if response != "stop":
                    print("Wallace: " + response)  # Log response
                    text_to_speech.speak(response)  # Speak out the response
                    
                elif response == "stop":
                    text_to_speech.speak("Goodbye, sir.")  # Say goodbye
                    return  # Exit the function
                else:
                    print("Wallace: " + response)  # Log error response
                    text_to_speech.speak("Sorry, I didn't catch that.")  # Speak error response
        except speech_recognition.UnknownValueError as err:
            recognizer = speech_recognition.Recognizer()  # Reset recognizer
            print("Error: " + err)  # Log error
            continue

def terminal_debug():
    """Enables terminal-based interaction with the chatbot."""
    while True:
        user_input = input("User: ")  # Get user input from the terminal
        response = speech.speech_to_text(user_input)  # Process user input to get response
        print("Wallace: " + response)  # Log AI response
        text_to_speech.speak(response)  # Speak out the response

if __name__ == "__main__":
    """Main function to choose between voice control and GUI mode."""
    user_input = input("Would you like to use voice or gui? (y|voice / n|gui / clear memory 'clear'): ")
    if user_input == "voice" or user_input == "y":
        voice()  # Start voice control mode
    elif user_input == "gui" or user_input == "n":
        gui_main()  # Start GUI mode
    elif user_input == "term":
        terminal_debug()
    elif user_input == "clear":
        json.dump([], open("data/configs/memory.json", "w"))

        user_input = input("Would you like to use voice or gui? (y|voice / n|gui): ")
        if user_input == "voice" or user_input == "y":
            voice()
        elif user_input == "gui" or user_input == "n":
            gui_main()
        elif user_input == "term":
            terminal_debug()
    else:
        print("Invalid input. Please try again.")
        exit()  # Exit the program on invalid input
