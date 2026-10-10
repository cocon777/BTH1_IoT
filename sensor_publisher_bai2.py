import json
import random
import sys
import time
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
DEVICE_ID = sys.argv[1] if len(sys.argv) > 1 else "sensor01"
TOPIC = f"iot/lab/{DEVICE_ID}/data"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        data = {
            "device_id": DEVICE_ID,
            "temperature": round(random.uniform(25, 40), 1),
            "humidity": round(random.uniform(30, 80), 1),
        }
        # Gui du lieu moi 3 giay
        client.publish(TOPIC, json.dumps(data))
        print(f"Da gui {TOPIC}: {data}")
        time.sleep(3)
except KeyboardInterrupt:
    print("Da dung sensor.")
finally:
    client.loop_stop()
    client.disconnect()
