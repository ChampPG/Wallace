# import speech_recognition as sr

# # obtain audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)


# # recognize speech using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))


# import speech_recognition as sr

# r = sr.Recognizer()
# mic = sr.Microphone()

# for device_index in sr.Microphone.list_microphone_names():
#     print(device_index)

# for device_index in sr.Microphone.list_working_microphones():
#     m = sr.Microphone(device_index=device_index)
#     print(m.device_index)
#     break
# else:
#     print("No microphone found.")


# import pyttsx3

# engine = pyttsx3.init()

# voices = engine.getProperty("voices")
# engine.setProperty("rate", 150)
# engine.setProperty("volume", 1)

# engine.setProperty("voice", voices[0].id)

# engine.say("Hello, my name is Wallace")

# engine.runAndWait()

# for voice in voices: 
#     # to get the info. about various voices in our PC  
#     print("Voice:") 
#     print("ID: %s" %voice.id) 
#     print("Name: %s" %voice.name) 
#     print("Age: %s" %voice.age) 
#     print("Gender: %s" %voice.gender) 
#     print("Languages Known: %s" %voice.languages) 


# import json, openai

# openai.api_key = json.load(open("openai.json"))["key"]
# openai.organization = json.load(open("openai.json"))["org"]

# response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt="Hello, my name is Wallace. How are you doing today?", max_tokens=100)

# print(response.choices[0].text)
# print(response)

# import requests, json

# prompt = "Hello Wallace, how are you doing today?"

# # URL and data for the request
# url = "http://10.20.0.31:8080/api/generate"
# data = {
#     "model": "wallace",
#     "prompt": prompt,
#     "stream": False
# }

# # Convert the data dictionary to a JSON string
# json_data = json.dumps(data)

# # Make the POST request
# response = requests.post(url, data=json_data)

# # Check if the request was successful and print the response
# if response.status_code == 200:
#     print(response.text)
# else:
#     print("Error:", response.status_code)
