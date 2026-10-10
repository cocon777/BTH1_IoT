import time
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/message"
HO_TEN = "Nguyen Minh Quyet"
MSSV = "B22DCCN677"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)
client.loop_start()

# Gui 5 thong diep lien tiep
for i in range(1, 6):
    payload = f"Xin chao tu client Python MQTT - {MSSV} - {HO_TEN} (#{i})"
    client.publish(TOPIC, payload).wait_for_publish()
    print(f"Da gui: {payload}")
    time.sleep(1)

client.loop_stop()
client.disconnect()
