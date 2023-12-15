# Wallace
Personal Home Assistant Bot


# Setup

## Requirements

### Python Dependencies

`pip install -r requirements.txt`


### Setting setup

## Google Api Setup
Sidenote: You must use a chrome based browser to properly do the authentication!

Follow this guide down to the "Install the Google client libray section"

Guide: https://developers.google.com/docs/api/quickstart/python

When you get the credentials file rename it to "credentials.json" then put it in the bin folder. From here you will want to run google_calendar.py this will generate a token file. You will see a test output in your terminal of your next events if this worked properly.

## Run the setup.py file
1. Run the setup.py and input information needed


## Optional
1. Setup url for api for the personal chatbot </br>
1.1. in the /etc/systemd/system/ollama.service file, you may also add
     `Environment="OLLAMA_HOST=0.0.0.0"`
2. Openai api key for search commands

## Required
1. voice_id
2. microphone_index

run and if you would like to setup all settings select 5 then select 6
`setup.py`

## Optional
**Linux**
* python3 -m venv venv
* source ./venv/bin/activate
**Windows**
* python3 -m venv venv
* souce .\venv\bin\activate.ps1

