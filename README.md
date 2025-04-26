# 🤖 Webots Robot Controller: Line Following 🚗

Welcome to the **Line Following Robot** project! This project demonstrates an autonomous robot in the **Webots simulation environment**, using **three line sensors** and **two motors** to navigate a track. The robot utilizes a **proportional control algorithm** (PID-like) to keep itself on track.

## 🔧 Project Components

The robot is built with the following components:

- **Line Sensors** (👁️): Three sensors (left, center, right) detect the line on the track.
- **Motors** (🛠️): Two motors (left and right) control the movement of the robot.
- **Controller** (⚙️): A **simple proportional control algorithm** guides the robot's movement to stay centered on the line.

## 📝 Prerequisites

Before you get started, make sure you have:

- **Webots Simulation Software** (🖥️): Installed and set up.
- **Robot Model** (🤖): A robot with **two motors** and **three line sensors**.

## 🚀 How to Use

Follow these simple steps to run the simulation:

1. Load the code in the **Webots environment**.
2. Connect the **controller** to the robot.
3. Start the **simulation**. Watch the robot follow the line automatically! 🎯

## 🌍 Environment Image

Here’s a visual representation of the environment where the robot operates. It shows the track, robot, and sensors in the Webots simulation.

![Robot Environment](path_to_image.jpg)  

## 🧠 PID Controller Explanation

### ⚙️ Proportional Control (PID)

The robot follows the track using a **proportional control** algorithm. The **error term** is calculated based on the readings from the three line sensors:
- **e = 0**: The center sensor detects the line, and the robot moves straight ahead.
- **e = 1**: The right sensor detects the line, causing the robot to steer left.
- **e = -1**: The left sensor detects the line, causing the robot to steer right.

The robot adjusts its motors using a **proportional constant** `kp`:
- **Base Speed**: The robot’s default speed.
- **Speed Adjustment**: The motor speeds are adjusted by adding or subtracting the error term, scaled by `kp`.

### 💻 PID Code Implementation

Here’s how the PID control is implemented:

```python
# Proportional control adjustment
kp = 50
u = kp * e
motor(BASE_SPEED + u, BASE_SPEED - u)
```

### 🔍 How the PID Code Works

- **Base Speed**: The robot’s base speed is set as a fraction of the maximum speed (`MAX_SPEED`).
- **Sensor Readings**: The robot continuously reads the values from the left, center, and right sensors to determine its position relative to the track.
- **Error Calculation**: The robot calculates the error (`e`) based on sensor input, which indicates its deviation from the track's center.
- **Motor Adjustment**: The motors' speeds are adjusted based on the error, guiding the robot back to the center of the track.

## 🎯 Expected Outcome

Once the simulation starts, the robot will **autonomously follow** the line by adjusting its movement based on the sensor feedback. The robot will stay on the track by making real-time corrections based on the error values. 🚗💨
