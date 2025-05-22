# 🗣️ Language Translation via Speech

This is a Python-based speech translation tool that:
- Captures speech from the microphone
- Translates it into a chosen language
- Speaks out the translated text

## 🚀 Features

- Speech-to-Text using `speech_recognition`
- Language Translation using `googletrans`
- Text-to-Speech using `gTTS` + `playsound`

## 🛠️ Requirements

```bash
pip install speechrecognition googletrans==4.0.0-rc1 gtts playsound pyaudio
