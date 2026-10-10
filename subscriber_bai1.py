from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/message"


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Ket noi broker: {reason_code}")
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    print("Nhan duoc message:")
    print(f"Topic: {msg.topic}")
    print(f"Payload: {msg.payload.decode('utf-8')}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}\n")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Da dung subscriber.")
    client.disconnect()
