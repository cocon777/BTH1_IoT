import json
import sys
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
DEVICE_ID = sys.argv[1] if len(sys.argv) > 1 else "sensor01"
TOPIC = f"iot/lab/{DEVICE_ID}/data"


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Ket noi broker: {reason_code}")
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode("utf-8"))
        temp = data["temperature"]
        hum = data["humidity"]
    except (json.JSONDecodeError, KeyError):
        print("Payload khong hop le:", msg.payload)
        return

    print(f"Device: {data.get('device_id')}")
    print(f"Temperature: {temp} C")
    print(f"Humidity: {hum} %")
    # Kiem tra nguong canh bao
    if temp > 35:
        print("CANH BAO: Nhiet do cao")
    if hum < 40:
        print("CANH BAO: Do am thap")
    print()


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Da dung monitor.")
    client.disconnect()
