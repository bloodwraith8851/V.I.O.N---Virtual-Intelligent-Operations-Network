# 🤖 V.I.O.N - Virtual Intelligent Operations Network

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

<img src="www/assets/img/VION.ico" alt="V.I.O.N Logo" width="150"/>

*Your intelligent desktop companion powered by voice commands* 🎙️

[Features](#-features) • [Architecture](#-architecture) • [Setup](#-setup-and-installation) • [Usage](#-usage) • [Customize](#-customizing-commands)

</div>

V.I.O.N is a desktop voice assistant built with Python and a web-based user interface. It leverages speech recognition to understand commands and text-to-speech to provide responses. The application features a dynamic and animated UI to visualize its listening and processing states.

## ✨ Features

- 🎤 **Voice Command Control**: Interact with your system using voice commands
- 🎨 **Dynamic UI**: A visually appealing interface featuring:
  - 🌐 Particle sphere visualization
  - 🌊 Siri-style wave animations
  - ✨ Animated text feedback
- 🚀 **Application and Website Launcher**: Open any system application or website with a simple "open" command
- 📺 **YouTube Integration**: Directly play videos on YouTube by voice command
- ⚙️ **Customizable Commands**: Easily add new applications and websites via SQLite database
- 🌉 **Cross-Platform Bridge**: Uses `eel` for seamless Python-JavaScript communication

## 🏗️ Architecture

The project is divided into two main components: the Python backend (engine) and the web-based frontend (www).

### 🛠️ Backend (`engine/`)

-   📄 **`main.py`**: Entry point, initializes `eel` web server and launches UI
-   🎯 **`engine/command.py`**: Handles speech recognition and text-to-speech
-   ⚡ **`engine/features.py`**: Core command execution logic
-   💾 **`engine/db.py`**: SQLite database schema management
-   🗄️ **`vion.db`**: SQLite database with tables:
    -   `sys_command`: Local application paths
    -   `web_command`: Website URLs

### 🎨 Frontend (`www/`)

-   📱 **`index.html`**: Main UI structure
-   🎭 **`style.css`**: UI styling and animations
-   🔧 **`main.js`**: Frontend logic and backend communication
-   🌟 **`script.js`**: 3D particle sphere animation
-   🎮 **`controller.js`**: UI update handling

## 🚀 Setup and Installation

> 💡 This project is optimized for Windows, using the `sapi5` TTS engine

1.  📥 **Clone the repository:**
    ```sh
    git clone https://github.com/bloodwraith8851/V.I.O.N---Virtual-Intelligent-Operations-Network.git
    cd V.I.O.N---Virtual-Intelligent-Operations-Network
    ```

2.  📦 **Install Python dependencies:**
    ```sh
    # Using virtual environment (recommended)
    pip install -r requirements.txt

    # Or manually install packages
    pip install eel pyttsx3 SpeechRecognition playsound pywhatkit PyAudio
    ```
    > ⚠️ **Note:** For `PyAudio` installation issues, visit [Christoph Gohlke's Unofficial Windows Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

3.  🎯 **Launch V.I.O.N:**
    ```sh
    python main.py
    ```

## 🎮 Usage

1.  🎤 **Activate V.I.O.N**: Click microphone icon or press `Win + V`
2.  🗣️ **Speak Commands**: Watch for the wave animation indicating listening mode
3.  📝 **View Feedback**: See recognized text and responses on screen

### 📝 Example Commands

-   💻 **Open Applications:**
    > "Open notepad"  
    > "Open android studio"

-   🎵 **YouTube Playback:**
    > "Play a song on youtube"  
    > "Play how to code on youtube"

## ⚙️ Customizing Commands

Extend V.I.O.N's capabilities through the SQLite database (`vion.db`).

### 📱 Add a New Application

1.  Open `vion.db` with DB Browser for SQLite
2.  Navigate to `sys_command` table
3.  Add new row:

    | id  | name            | path                                       |
    | --- | --------------- | ------------------------------------------ |
    | ... | ...             | ...                                        |
    | 3   | visual studio   | C:\Program Files\Microsoft Visual Studio\... |
    
### 🌐 Add a New Website

1.  Open `vion.db` with DB Browser for SQLite
2.  Navigate to `web_command` table
3.  Add new row:

    | id  | name     | url                      |
    | --- | -------- | ------------------------ |
    | ... | ...      | ...                      |
    | 2   | github   | https://www.github.com/  |

---

<div align="center">

Made with ❤️ by [bloodwraith8851](https://github.com/bloodwraith8851)

</div>