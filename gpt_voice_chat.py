#!/usr/bin/env python3
# This script will generate a chat using the microphone and computer to talk to each other
# This Works - Use this script - added script to output the conversation to a file gpt_voice.txt

import pyttsx3
import speech_recognition as sr
import openai
import sounddevice as sd
import soundfile as sf
import datetime
from alive_progress import alive_bar
import time

with alive_bar(100) as bar:
    for i in range(100):
        time.sleep(0.1)
        bar()

# Sampling frequency
fs = 44100

# Set up the OpenAI API client
openai.api_key = "sk-Add-Your-Own-OpenAI-API-Key-Here"

# Set up text-to-speech engine
engine = pyttsx3.init()
# Set the voice speed
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  # Decrease the speed by 50

# Set up conversation variables
conversation_history = ""
user_name = "My Lord"
bot_name = "Jervis"

# Define the OpenAI GPT-3 model
model_engine = "text-davinci-003"

# Define function to process user input
def process_input(user_input):
    global conversation_history
    prompt = user_name + ": " + user_input + "\n" + bot_name + ": "
    conversation_history += prompt
    response = openai.Completion.create(
        engine=model_engine,
        prompt=conversation_history,
        max_tokens=2048,
        temperature=0.9
    )
    response_text = response.choices[0].text.strip()
    conversation_history += response_text + "\n"
    print(bot_name + ": " + response_text)
    engine.say(response_text)
    engine.runAndWait()
    log_conversation(user_input, response_text)
    
# Initialize the speech recognizer
r = sr.Recognizer()

# Define the microphone as the audio source
mic = sr.Microphone()

# Define the prompt for the bot to start listening
bot_prompt = "🤖 My Lord, you can ask a question now!"

# Define the bot's introduction message
intro_message = "🤖 What can I help you with My Lord?"

# Define a flag to keep the conversation going
conversation_active = True

# Function to log the conversation to a text file
def log_conversation(user_input, bot_response):
    with open("gpt_voice.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(timestamp + " " + user_name + ": " + user_input + "\n")
        f.write(timestamp + " " + bot_name + ": " + bot_response + "\n")

# Start the conversation loop
engine.say("My Lord, you can ask a question now!")
engine.runAndWait()
while conversation_active:
    with mic as source:
        print(bot_prompt)
        audio = r.listen(source)

    try:
        # Use the speech recognizer to convert speech to text
        user_input = r.recognize_google(audio)

        # Print the user's input
        print("User:", user_input)
        
        if user_input.lower() == "goodbye":
            print("Goodbye My Lord!")
            engine.say("Goodbye My Lord!")
            engine.runAndWait()
            conversation_active = False
            break

        # Process the user's input and generate a response from the bot
        process_input(user_input)

        # Prompt the user to continue the conversation
        # bot_prompt = "🤖 What else can I help you with My Lord?"
        
        # Prompt the user to continue the conversation
        bot_prompt = "What else can I help you with My Lord?"
        print(bot_prompt)
        engine.say(bot_prompt)  # speak the prompt using pyttsx3
        engine.runAndWait()

    except sr.UnknownValueError:
        # If speech is unintelligible, print a message and prompt the user to try again
        print("I'm sorry My Lord, I didn't understand what you said. Please try again.")
        bot_prompt = "Please try again."

    except sr.RequestError as e:
        # If there's an issue with the speech recognizer, print an error message
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        bot_prompt = "Please try again."

