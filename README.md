# converse-with-chat-gpt-using-your-voice

<h1 align="center">Hi, guys! <img src="https://github.com/FujiwaraChoki/FujiwaraChoki/blob/main/assets/238178097-766d336d-b87d-44ba-807c-c51de2bc6b4d.gif" width="28px" alt="👋"></h1>

![PowerShell](https://img.shields.io/badge/-PowerShell-black?style=flat-square&logo=powershell)

![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/jervis-ChatGPT?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/jervis-ChatGPT?style=flat-square)

<b>Languages</b>

[![Python](https://img.shields.io/badge/python-black?style=for-the-badge&logo=python)](https://github.com/davidtkeane)

<b>OS</b>

[![Linux](https://img.shields.io/badge/linux-black?style=for-the-badge&logo=Linux)](https://github.com/davidtkeane)
[![Windows](https://img.shields.io/badge/Windows-black?style=for-the-badge&logo=Windows)](https://github.com/davidtkeane)

<p align="center">
    <b>Welcome to ChatGPT on the command line uses with API!</b>
    <br>
    <br>
    <i>
        I'm Rangersmyth (internet name), and I'm currently learning Python and Bash coding.<br>
    <br>
    </i>
    <br>

<p align="center">
  <img src="https://count.getloli.com/get/@rangersmyth?theme=gelbooru" />
</p>

<div align="center">
<a href="https://github.com/davidtkeane" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://twitter.com/davidtkeane" target="_blank">
<img src=https://img.shields.io/badge/twitter-%2300acee.svg?&style=for-the-badge&logo=twitter&logoColor=white alt=twitter style="margin-bottom: 5px;" />
</a>
<a href="https://linkedin.com/in/sami-hindi-b31435248/" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>
</div>

# About

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
5. Run the script using `python gpt_voice_chat.py`.
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

