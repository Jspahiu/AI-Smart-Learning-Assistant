# AI Smart Learning Assistant with OPENAI Chatbot with Face Detection & Voice Interaction

## 👋 About Me
I'm a passionate 12-year-old student with a strong interest in Python and Artificial Intelligence. My favorite projects involve AI, and some game development. I am also in the Hack Club for extra support for my projects.

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

---

## 💡 Key Technologies

- **Python**
- face_recognition (Computer Vision)
- OpenAI Whisper (Speech Recognition)
- OpenAI RAG (GEN AI)
- ElevenLabs TTS (Speech Synthesis)

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

## Extra Infomation
Slides For Extra Info:
https://www.canva.com/design/DAGtr9JIF9c/WJH7KuGL-aDJ_i0GtBn2MQ/view?utm_content=DAGtr9JIF9c&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h86fe98d52c

Website For Extra Info:
https://jspahiu.github.io/AI_Smart_Learning_Assistant/
