# AI Smart Learning Assistant with OPENAI Chatbot with Face Detection & Voice Interaction

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.11%20--%203.12-brightgreen?)

## Summer of Making 2025 for the Hack Club! ##

![How it Works!](README%20Images/Readme_Image1.png)

## 🔗 Useful Links

- 🌐 [Information Website](https://jspahiu.github.io/AI_Smart_Learning_Assistant_Website/) - **Which also includes the links below!**
- 🌐 [Hack Club Summer Making Project Link](https://summer.hackclub.com/projects/7469) - **Vote/Follow this project here!!**
- 🎥 [Demo Video](https://www.youtube.com/watch?v=...)
- 🖼️ [Canva Slides](https://www.canva.com/design/DAGtr9JIF9c/WJH7KuGL-aDJ_i0GtBn2MQ/view?utm_content=DAGtr9JIF9c&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h86fe98d52c)

---

## 👋 About Me
I’m a passionate 12-year-old student who loves building with Python and AI. I created this project to explore how AI can interact with people in fun and smart ways!

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
- SpeechRecognition (Old Speech Recognition Package) - **Not Currently Used in v2.0.0 or above**
- Pyttsx3 (Old TTS - Text to Speech Package) - **Not Currently Used in v2.0.0 or above**
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
- Yt_dlp (Used for finding the youtube video) - **LINUX ONLY**
- Vlc (Used for playing the youtube video) - **LINUX ONLY**


---

# 🏃 How to Run the Program (LOCALLY)

## For Linux (Raspberry Pi 5 - Raspberry Pi OS)
![Python](https://img.shields.io/badge/python-3.11-brightgreen)

---

## For Macs (M Series)
**Mac Requirements**:
- **Supported Device** (The Mac)
- **Terminal with Git**
- **![Python](https://img.shields.io/badge/python-3.12-brightgreen)** (Mac)
- **Code Editor or Normal Editor**
- **Really Good Internet**

*Or watch this video [**here**]("example") for a tutorial on how to run on Mac!*

1. Open a new folder somewhere to put the code for the program
Open a new terminal and lead your terminal to your directory by doing this below
```bash
cd your_folder_path
```

2. Once you located your terminal to your path, run this below to download the files directly from the project’s github repo:
```bash
git clone https://github.com/Jspahiu/AI-Smart-Learning-Assistant.git
```

3. Find the folder in your path named, “**AI-Smart-Learning-Assistant**” 

4. Open the folder and delete the folder that does not support the Mac which is named (Linux (Raspberry Pi 5)).

5. Also if you want, you may as well delete the readmes if you want to access the readme via Github

6. In your terminal, we need to direct our terminal to our folder named, “M Series Macs”, so type this command below,
```bash
cd “AI-Smart-Learning-Assistant/M Series Macs”
```

**If you get too many arguments error, follow below**
```bash
cd AI-Smart-Learning-Assistant
```
```bash
cd "M Series Macs"
```

7. **(Highly Recommended Step)** - Here is how to make a virtual environment since we have a lot of big packages with a lot of dependencies,
- **Best to use ![Python](https://img.shields.io/badge/python-3.12-brightgreen) since that is what the code has been tested on**
```bash
python3.12 -m venv venv
```

8. **(For Virtual Environments Only)** - Then to connect to the Virtual Environment that we made, enter the command below,
```bash
source venv/bin/activate
```
- **Check Python Version if it is ![Python](https://img.shields.io/badge/python-3.12-brightgreen)**
```bash
python --version
```
**It should end up something like this below**
```bash
Python 3.12.0
```

9. To install the packages, enter the command below. But beware this can take quite a while depending on what type of Mac it is (Really only should be worried on a Intel Mac)
```bash
pip install -r requirements.txt
```

If you succeed with the installation, congrats, you made it through the toughest part of running this program! 

10. Open a editor to enter our api keys in a file named, “**.env**”, which in it, it should have keys like this - 

```bash
OPENAI_API_KEY=sk-proj-
ELEVENLABS_API_KEY=sk-
```

- For the **OPENAI_API_KEY**, get from **OpenAi’s** platform website, [**https://platform.openai.com/api-keys**](https://platform.openai.com/api-keys), which you should get the api key **(Highly Recommended to get some credits for GPT model usage)**

- For the **ELEVENLABS_API_KEY**, go to their website at [**https://elevenlabs.io/app/settings/api-keys**](https://elevenlabs.io/app/settings/api-keys), where you can find the API key for **Elevenlabs**!

11. Once you got your API keys, we need to add an image of yourself for the Face Recognition Model. So all you need to do is to put that image of yourself in the folder named, “**images**”.

12. Make sure that you have the **right camera_id and mic_index** for your computer which is located in **Config.py**!
```bash
camera_id = 0

# Replace this with the correct microphone index
mic_index = 1  # Change to the index of your USB microphone
```

13. Make sure once again that you are in the right folder in your terminal named “**M Series Macs**”, and that you are connected to the **virtual environment**

14. Run the python command below to finally run the program,
```bash
python my_voice_and_video_chatbot.py
```
## How to Use Notes

### --- How To Use --- ###
1. When the program runs, **always put your face in front of your camera**, unless you want to leave the program paused!
2. Then **ask a question** based from the question available from [**here**](https://docs.google.com/document/d/1uVEmKQHGqlVKLykhiiiROP3_XhXZwjbI1lflShMULNk/edit?usp=sharing).
3. **Wait** for the **question** to **finish**.
4. To **exit the program**, say the word,"**Goodbye**", which should exit the program. If that does not work, do a keyboard interrupt by entering on your keyboard, **Control-C**.
###

### --- Configuring Program Details ---

1. For the **RAG LLM**, if you want to **save and create the FAISS Database** please turn this below in line 50,
```bash
self.chatbot = Chatbot(["data_sets/Bill of Rights Full.pdf", "data_sets/Floor_Hockey.pdf", "data_sets/electric_cars_america.pdf", "data_sets/global_warming.pdf", 
                                "data_sets/Justicia_Carnea.pdf", "data_sets/The Veldt.pdf", "data_sets/Nerves System.pdf", "data_sets/Parts Of Cells.pdf"]
                                , False)
```
- To this, and what we are only changing is turning **False** to **True**!
```bash
self.chatbot = Chatbot(["data_sets/Bill of Rights Full.pdf", "data_sets/Floor_Hockey.pdf", "data_sets/electric_cars_america.pdf", "data_sets/global_warming.pdf", 
                                "data_sets/Justicia_Carnea.pdf", "data_sets/The Veldt.pdf", "data_sets/Nerves System.pdf", "data_sets/Parts Of Cells.pdf"]
                                , True)
```
- **After saving the database while running the program, make sure you asked a question to save your database and then change the True to False in line 50 for faster response times**

2. For **Elevenlabs Voice ID**, please go to their website [**here**](https://elevenlabs.io/) and copy the Voice ID in the voice you selected to use and enter it in the file named, **Config.py**, which the line below is in **line 15**.
```bash
VOICE_ID = "3NFDHTNDKqip06i6bFkQ" # <------ Or Whatever Voice ID You Want!
```

3. For **other voice** settings, you can configure in **Config.py** which starts from **line 24** to **line 32**!
```bash
RECORD_SECONDS = 5
FILENAME = "temp.wav"
SAMPLERATE = 44100  # CD-quality audio

SAMPLE_RATE = 16000
CHANNEL = 1
FRAME_DURATION = 30  # ms
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION / 1000)
MAX_SILENCE_FRAMES = 15  # ~0.5 seconds of silence
```

###


##


---

## For Non-Listed Devices


- Windows computers are sadly not compatible due to module supporting issues (face_recongition)
- If you have an older pi like (Pi 4 or older), be aware of performance issues and compatibility issues since not have been tested on there
- If you are running Linux but another machine or/and a different computer, follow the Linux tutorial but it has not been tested on any other Linux OS (Except Raspberry Pi OS).
- If you are running a Intel Mac, make sure you at least have a OS new enough for ![Python](https://img.shields.io/badge/python-3.12-brightgreen)

**SO NO GUARANTEE OR IMPOSSIBLE IT WILL WORK IF YOU DO NOT HAVE DEVICES WITH BOLD TEXT ABOVE**

---

## 🚲 Hobbies & Motivation

I enjoy combining my love for programming and AI to make fun and useful things. This project is inspired by my passion for making technology fun, interactive, and accessible!

---

## ✨ Future Plans

- Add more commands (home automation, flight info (via API))
- Enhance voice customization (With popular character voices)
- Adding a web version accessible to everyone

---

## 🗳️ Vote/Follow (If you are in the Hack Club)

If you like my project, please vote or follow for me for future support of this project!

## 🔗 Useful Links

- 🌐 [Information Website](https://jspahiu.github.io/AI_Smart_Learning_Assistant_Website/) - **Which also includes the links below!**
- 🌐 [Hack Club Summer Making Project Link](https://summer.hackclub.com/projects/7469) - **Vote/Follow this project here!!**
- 🎥 [Demo Video](https://www.youtube.com/watch?v=...)
- 🖼️ [Canva Slides](https://www.canva.com/design/DAGtr9JIF9c/WJH7KuGL-aDJ_i0GtBn2MQ/view?utm_content=DAGtr9JIF9c&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h86fe98d52c)
---
