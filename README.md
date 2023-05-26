# converse-with-chat-gpt-using-your-voice
This script uses the OpenAI GPT-3 model and speech recognition to generate a chat between the user and the bot using the microphone and computer to talk to each other. The conversation history is logged to a text file, and the bot's responses are spoken aloud using Pyttsx3.

## GPT-3 Voice Chat

This script uses the OpenAI GPT-3 model and speech recognition to generate a chat between the user and the bot using the microphone and computer to talk to each other. The conversation history is logged to a text file, and the bot's responses are spoken aloud using Pyttsx3.

### Installation and Usage

1. Clone or download this repository. This will work for all platforms.
2. Install the required modules by running `pip install -r requirements.txt`.
💡  Just remove the following module to install on either windows or linux.
💡  The module SpeechRecognition for windows and speech_recognition is for linux      
💡  pip install PyAudio & pip install SpeechRecognition for windows.     
3. Make sure you have an OpenAI API key. If you don't have one, go to [https://beta.openai.com/signup/](https://beta.openai.com/signup/) to sign up for early access and get an API key.
4. In the script, replace "YOUR_API_KEY" with your API key.
5. Run the script using `python gpt_voice.py`.
6. A text file called gpt_voice.txt will be created once you have started the voice recognition script, this will save the conversation with timestamps.

### Improvements

- Add error handling for cases where the mic or sound devices are not available.
- Implement a GUI to make the chat more user-friendly.
- Allow the user to choose which voice the bot should use.
- Improve the accuracy of the speech recognition by using a custom language model.
- Add support for multiple languages. 

### Requirements

- The script requires the following modules: If any problem is encountered install manually $ pip install or pip3 install modulename.
- speech_recognition is a linux module and SpeechRecognition is for windows.

```
pyttsx3
speech_recognition
openai
sounddevice
soundfile
SpeechRecognition
alive_progress
PyAduio
```

