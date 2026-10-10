import json
import sys
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
DEVICE_ID = sys.argv[1] if len(sys.argv) > 1 else "light01"
CMD_TOPIC = f"iot/lab/{DEVICE_ID}/cmd"
STATUS_TOPIC = f"iot/lab/{DEVICE_ID}/status"

state = "OFF"


def publish_status(client):
    payload = json.dumps({"device_id": DEVICE_ID, "status": state})
    client.publish(STATUS_TOPIC, payload)
    print(f"Da gui trang thai: {payload}")


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"{DEVICE_ID} ket noi broker: {reason_code}")
    client.subscribe(CMD_TOPIC)
    publish_status(client)


def on_message(client, userdata, msg):
    global state
    cmd = msg.payload.decode("utf-8").strip().upper()
    print(f"Nhan lenh: {cmd}")
    # Chi cap nhat trang thai va phan hoi khi lenh hop le
    if cmd in ("ON", "OFF"):
        state = cmd
        publish_status(client)
    else:
        print("Lenh khong hop le, bo qua.")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Da tat thiet bi.")
    client.disconnect()
