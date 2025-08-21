# 🏠 Smart Home IoT Simulator

This project is a simple **IoT Smart Home simulator** built with Python and MQTT.  
It simulates basic smart devices like **Lights, Fan, and Door Lock/Unlock** and shows how they can publish and subscribe to MQTT topics.

---

## 🚀 Features
- Turn **Lights** ON/OFF
- Turn **Fan** ON/OFF
- Lock/Unlock **Door**
- Real-time communication between publisher and subscriber
- Uses **MQTT Broker** for message passing

---

## 📂 Project Structure
smart_home_sim/
── smart_home_sim.py   # Publishes commands (Light, Fan, Door) Also Subscribes & listens to device updates
── README.md                 # Project documentation

## ▶️USAGE
In a New Terminal run
python smart_home_sim.py

## 📸Example Output
Sent: Light ON
Received: Light ON on topic iot/smart_home/devices

Sent: Door Locked
Received: Door Locked on topic iot/smart_home/devices

## 🎯 Future Improvements
	•	Add more devices (AC, TV, Sensors)
	•	Create a GUI dashboard
	•	Deploy on Raspberry Pi / ESP32 for real hardware simulation

⸻

## 👨‍💻 Author

Made  by Tauqeer Zia



