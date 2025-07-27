# AI Smart Learning Assistant with OPENAI Chatbot with Face Detection & Voice Interaction


![How it Works!](README%20Images/Readme_Image1.png)

## 🔗 Useful Links

- 🌐 [Infomation Website](https://jspahiu.github.io/AI_Smart_Learning_Assistant_Website/) - **Which also includes the links below!**
- 🌐 [Hack Club Summer Making Project Link](https://summer.hackclub.com/projects/7469)
- 🎥 [Demo Video](https://www.youtube.com/watch?v=...)
- 🖼️ [Canva Slides](https://www.canva.com/design/DAGtr9JIF9c/WJH7KuGL-aDJ_i0GtBn2MQ/view?utm_content=DAGtr9JIF9c&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h86fe98d52c)

---

## 👋 About Me
I'm a passionate 12 year old student with a strong interest in Python and Artificial Intelligence. My favorite projects involve AI, and some game development. I am also in the Hack Club for extra support for my projects.

---

## 📝 Project Description

This project is an advanced AI assistant that interacts with users only when their face is detected. It combines computer vision, speech recognition, and state-of-the-art AI to provide a truly hands-free and interactive experience. All responses are spoken aloud using realistic TTS voices!

### 🔄 How It Works

1. **Face Detection**  
   Uses the [face_recognition](https://github.com/ageitgey/face_recognition) library to detect when a person's face is present.

2. **Speech Input (STT)**  
   Once a face is detected, the user can ask questions using their voice. Speech is transcribed using [Whisper](https://github.com/openai/whisper).

3. **Intelligent Response System**  
   - If the user asks about the time, weather, or wants to play YouTube videos (Linux only), the program handles those directly.
   - For general questions, the input is sent to OpenAI’s RAG (Retrieval-Augmented Generation) model, which answers based on the provided data sets (PDF).

4. **Text-to-Speech Output**  
   The response is spoken back to the user using [ElevenLabs TTS](https://elevenlabs.io/) for realistic, human-like voices.


![How it Works!](README%20Images/Readme_Image1.png)

---

## 💡 Key Technologies

**Made with 100% Python with packages included below**

**Main Packages**:

- OS and Dotenv (Getting API Keys from .env files)
- SpeechRecognition (Old Speech Recognition Package)
- Pyttsx3 (Old TTS - Text to Speech Package)
- ElevenLabs (New TTS - Text to Speech Package)
- Whisper (Used for STT - Speech to Text, New Speech Recognition Package)
- Sounddevice (Recording Audio)
- Soundfile (Write Audio File for Whisper)
- Numpy (Getting Full Audio from SoundDevice, Getting Best Match Index using the Argmin function in numpy which finds the smallest number in an array)
- Webrtcvad (Stops the listening process when the person stops talking)
- Glob (Getting Image Files for Face Recognition)
- FaceRecognition (Current Face Recognition Package)
- Langchain (For LLM, PDF Files Loader, and Vector Database)
- OpenAI (Gen AI)
- FAISS (Gen AI)
- Threading (For MultiThreading Use)
- Python Cv2 (See your face detected in a window)
- Pygame (Fix Cv2 Window)

**Other Packages**:

- Random (For random welcomes!)
- Datetime (Check Time, Give Time of Day Welcomes)
- Geocoder (Track Location including latitude and longitude for weather API)
- Requests (Uses Open-Meteo API keys to find the weather and temperature in the area for weather question and for random greetings)
- Yt_dlp (Used for finding the youtube video)(LINUX ONLY)
- Vlc (Used for playing the youtube video)(LINUX ONLY)


---

# 🏃 How to Run the Program (LOCALLY)

## For Linux (Raspberry Pi 5 - Raspberry Pi OS)


---

## For Macs (M Series)

---

## For Non-Listed Devices


- Windows computers are sadly not compatible due to module supporting issues (face_recongition)
- If you have an older pi like (Pi 4 or older), be aware of performance issues and compatibility issues since not have been tested on there
- If you are running linux but another machine or/and a different computer, follow the linux tutorial but not have been tested on other OS (Only Raspberry Pi OS).
- If you are running a intel mac, make sure you at least have a OS new enough for Python 3.12

**SO NO GUARANTEE OR IMPOSSIBLE IT WILL WORK IF YOU DO NOT HAVE DEVICES WITH BOLD TEXT**

---

## 🚲 Hobbies & Motivation

I enjoy combining my love for programming and AI to make fun and useful things. This project is inspired by my passion for making technology fun, interactive, and accessible!

---

## ✨ Future Plans

- Add more commands (home automation, flight info (via API))
- Enhance voice customization (With Popular Character voices)
- Adding a web version accessible to everyone

---

## 🗳️ Vote (If you are in the Hack Club)

If you like my project, please vote for me for future support of this project!

## 🔗 Useful Links

- 🌐 [Infomation Website](https://jspahiu.github.io/AI_Smart_Learning_Assistant_Website/) - **Which also includes the links below!**
- 🌐 [Hack Club Summer Making Project Link](https://summer.hackclub.com/projects/7469)
- 🎥 [Demo Video](https://www.youtube.com/watch?v=...)
- 🖼️ [Canva Slides](https://www.canva.com/design/DAGtr9JIF9c/WJH7KuGL-aDJ_i0GtBn2MQ/view?utm_content=DAGtr9JIF9c&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h86fe98d52c)
---