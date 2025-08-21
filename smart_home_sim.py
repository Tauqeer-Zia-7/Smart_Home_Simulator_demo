import paho.mqtt.client as mqtt
import time
import threading

# MQTT settings
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/smart_home/devices"

# Called when client connects
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
        client.subscribe(TOPIC)
    else:
        print("❌ Connection failed")

# Called when message received
def on_message(client, userdata, msg):
    print(f"📩 Received: {msg.payload.decode()} on topic {msg.topic}")

# Publisher loop (sends commands)
def publisher(client):
    commands = ["Light ON", "Fan ON", "Fan OFF", "Door Locked", "Door Unlocked"]
    for cmd in commands:
        client.publish(TOPIC, cmd)
        print(f"📤 Sent: {cmd}")
        time.sleep(2)

# Initialize client
client = mqtt.Client("SmartHomeSim")
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker
client.connect(BROKER, PORT, 60)

# Run subscriber in background
threading.Thread(target=client.loop_forever, daemon=True).start()

# Run publisher
publisher(client)

# Keep program alive
while True:
    time.sleep(2)