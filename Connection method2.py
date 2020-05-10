import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK")
        global connection
        connection = True                # Set Flag
    else:
        print(" 'Bad connection' Returned code = ",rc)

connection = False  
client = mqtt.Client("MQTT")
client.on_connect = on_connect
client.loop_start()
client.connect('117.170.84.60', 18879)        # simply set the Broker IP and Port number Directly


# --- OUTPUT --- #

Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========================= RESTART: F:\python\Method2.py ========================
>>> connected OK

