import paho.mqtt.client as mqtt
import serial, time, json

ser = serial.Serial(port = '/dev/ttyACM0', baudrate=115200, timeout=1) 
print("Conexion establecida")
print(['eje x', 'eje y', 'eje z', 'Bateria baja', 'Trans'])

client = mqtt.Client("B77867")
client.connected = False

topic = 'v1/devices/me/telemetry'
client.username_pw_set('py74q1v0f1rfjvereeer')
client.connect("iot.eie.ucr.ac.cr", 1883)
dict = dict()

while(1):
    datos = ser.readline().decode('utf-8').replace('\r', "").replace('\n', "")
    datos = datos.split('\t')
    if len(datos) >= 3:
        dict["x"] = datos[0]
        dict["y"] = datos[1]
        dict["z"] = datos[2]

        if(datos[3] == "1"):
            bat_lv = "Bien"
        else:
            bat_lv = "Bajo"

        if(datos[4] == "1"):
            transmi = "Si"
        else:
            transmi = "No"
            bat_lv = ""

        dict["Bateria baja"] = bat_lv
        dict["Transmi"] = transmi
        mensaje = json.dumps(dict)
        print(mensaje)
        client.publish(topic, mensaje)
        client.loop()


    

