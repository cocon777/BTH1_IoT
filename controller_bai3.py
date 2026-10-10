import sys
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
DEVICE_ID = sys.argv[1] if len(sys.argv) > 1 else "light01"
CMD_TOPIC = f"iot/lab/{DEVICE_ID}/cmd"
STATUS_TOPIC = f"iot/lab/{DEVICE_ID}/status"


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Ket noi broker: {reason_code}")
    client.subscribe(STATUS_TOPIC)


def on_message(client, userdata, msg):
    print("\nTrang thai nhan duoc:")
    print(msg.payload.decode("utf-8"))


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        cmd = input("Nhap lenh (ON/OFF/EXIT): ").strip().upper()
        if cmd == "EXIT":
            break
        # Chan lenh sai truoc khi publish
        if cmd not in ("ON", "OFF"):
            print("Lenh sai, chi nhan ON hoac OFF.")
            continue
        client.publish(CMD_TOPIC, cmd)
        print(f"Da gui lenh {cmd} toi {DEVICE_ID}")
except KeyboardInterrupt:
    pass
finally:
    client.loop_stop()
    client.disconnect()
