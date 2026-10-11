# Thuc hanh MQTT voi Python

Sinh vien: Nguyen Minh Quyet - B22DCCN677
Nguyen Van Nguyen - B23DCCN615

## Cai dat

```bash
pip install -r requirements.txt
```

## Broker

Mac dinh dung broker public `broker.hivemq.com`, port `1883`, khong can tai khoan.
Muon doi broker (vi du Mosquitto local), sua hang so `BROKER` o dau moi file `.py`.

Chay Mosquitto local:

```bash
mosquitto -v
```

Sau do doi `BROKER = "localhost"`.

## Cach chay (mo moi chuong trinh trong 1 terminal rieng)

### Bai 1
```bash
python subscriber_bai1.py
python publisher_bai1.py
```

### Bai 2
```bash
python monitor_subscriber_bai2.py
python sensor_publisher_bai2.py
```
Chay nhieu thiet bi: `python sensor_publisher_bai2.py sensor02` va `python monitor_subscriber_bai2.py sensor02`.

### Bai 3
```bash
python device_bai3.py
python controller_bai3.py
```
Nhap `ON`, `OFF` hoac `EXIT`. Co the doi thiet bi: `python device_bai3.py fan01` va `python controller_bai3.py fan01`.

## Ket qua

- Bai 1: publisher gui 5 thong diep, subscriber in topic, payload, thoi diem nhan.
- Bai 2: sensor gui JSON moi 3 giay, monitor canh bao khi nhiet do > 35 C hoac do am < 40 %.
- Bai 3: dieu khien den ON/OFF hai chieu qua topic `cmd` va `status`, xu ly lenh sai.
