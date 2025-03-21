# Unreal-Engine-HeartBeat-Vis

## 🔧 Project Title: Real-Time Heartbeat Visualization in Unreal Engine

### 🔹 Project Overview:

This project captures real-time heartbeat data using an ESP32 and a pulse sensor, processes the data through Python, and visualizes it in Unreal Engine. It demonstrates how real-world biometric data can be integrated into interactive digital environments.
[Heartbeat Visualization](Media/HearthBeat.mp4)

---

## ✨ Project Stages:

### 🚀 Stage 1: Capturing Heartbeat Data with ESP32

#### Goal:

Collect heartbeat signals using a pulse sensor and send them over serial communication via ESP32.

#### Key Points:

- Pulse sensor connected to ESP32 on analog pin 36.
- Uses `PulseSensorPlayground` library to detect heartbeats.
- Calculates BPM (beats per minute) and sends the values over the serial port.
- **Threshold Adjustment:** The **threshold value** should be adjusted based on the specific sensor being used. We set it to **550**, but users should fine-tune this value according to their own sensor for accurate heartbeat detection.

---

### 💻 Stage 2: Sending Data to Unreal Engine with Python

#### Goal:

Read serial data from ESP32 and send it to Unreal Engine over a TCP socket using Python.

#### Requirements:

- Python 3.10
- `pyserial` library

#### Setup Steps:

1. Ensure Python 3.10 is installed.

2. (Optional) Create and activate a virtual environment:

3. Install dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Python script:

   ```bash
   python Main.py
   ```

#### Important Notes:

- The **serial port (COM8)** in the Python script must be set correctly according to your system. Change this if necessary.
- The script continuously listens for data and forwards it via TCP to Unreal Engine.

---

### 🎮 Stage 3: Visualizing the Data in Unreal Engine

#### Goal:

Receive heartbeat data in Unreal Engine and visualize it in real time.

#### Steps:

1. Ensure the **TCP Socket Plugin** is installed and enabled.
2. Open the **TestMap** level inside Unreal Engine.
3. Click `Simulate`. If everything is set up correctly, the project will start visualizing the heartbeat data.

Your Unreal project should include the following assets:

- **BP\_HeartConnection** (Blueprint handling TCP communication)
- **M\_HeartEquation** & **M\_HeartEquation\_Inst** (Materials for visual effects)
- **TestMap** (Level where the simulation runs)

If everything is properly set up, running the simulation will allow you to see the heartbeat data-driven visuals in action.

---

## 📄 Summary:

This project bridges the physical and virtual worlds by converting real heartbeat data into immersive game engine visuals. It can be extended with other biometric sensors and interaction methods for art installations, health visualizations, or biofeedback games.

Ready to visualize your heart in pixels. ❤️

