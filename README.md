# 🎵 Music with Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/toxicbishop/Music-with-python/graphs/commit-activity)

A modular and versatile music player ecosystem built with Python. From a lightweight CLI to a feature-rich modern GUI, this project offers multiple ways to enjoy your local music library.

---

## 🚀 Quick Start (Latest Version)

To dive straight into the most advanced version (GUI v2):

```powershell
# Navigate to the latest version
cd Music-Player-GUI-version-2


---

## 📂 Evolution of the Project

This repository tracks the development of the music player through three distinct phases:

### 💎 [GUI Version 2](./Music-Player-GUI-version-2/) (Latest)
The most advanced iteration with a focus on User Experience.
- **Playlist Sidebar**: Real-time discovery of all tracks in your library.
- **Smart Navigation**: Sequential playback with `Next` and `Previous` controls.
- **Volume Management**: Integrated slider for precise audio control.
- **Modern UI**: Sleek, responsive layout built with `customtkinter`.

### 🛠️ [GUI Version 1](./Music-Player-GUI-version-1/)
The initial transition from CLI to Graphical Interface.
- Simple, distraction-free playback.
- Single-file focus for testing core GUI logic.
- Lightweight and fast.

### 📜 [CLI Version](./music.py) (Legacy)
The core engine that started it all.
- Terminal-based selection and control.
- Zero GUI overhead.
- Perfect for low-resource environments.

---

## ✨ Key Features

*   **🔍 Auto-Discovery**: Automatically scans the `music_files/` directory for `.mp3` and `.wav` files.
*   **🎹 Intuitive Controls**: Full Play/Pause/Resume/Stop functionality across all versions.
*   **🎨 Premium Aesthetics**: High-quality dark mode visuals powered by CustomTkinter.
*   **🔊 Audio Engine**: Robust playback engine powered by the industry-standard `pygame.mixer`.

---

## 🛠️ Installation & Prerequisites

Ensure you have Python 3.x installed. Then, install the required dependencies:

```bash
pip install pygame customtkinter Pillow
```

### Setup your Library
1. Ensure the `music_files/` folder exists in the root.
2. Drop your favorite music files (.mp3 or .wav) into that folder.
3. Launch any version of the player!

---

## 📂 Project Structure

```text
.
├── Music-Player-GUI-version-1/  # v1 Release
├── Music-Player-GUI-version-2/  # v2 Release (Premium)
├── music_files/                 # Your Audio Assets
├── music.py                     # Legacy CLI Script
├── LICENSE                      # MIT License
└── README.md                    # Project Documentation
```

---

## 🎮 Controls (CLI Mode)

| Action | Key | Description |
| :--- | :--- | :--- |
| **Pause** | `P` | Pauses current track |
| **Resume** | `R` | Resumes from pause |
| **Stop** | `S` | Returns to menu |

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/toxicbishop">toxicbishop</a>
</p>
