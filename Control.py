import paho.mqtt.client as mqtt
from time import sleep

broker = "117.170.84.60"
port = 18879

def on_publish(client, userdata, result):     # creating publish bind to call back
    print("data published \n")                # prints if data published when the While statement is True
    pass

# Call Back functions

client = mqtt.Client("MQTT")
client.connect(broker, port)                  # calling the broker and port
client.on_publish = on_publish                # calling the publish bind
client.loop_start()                           # starts to show publish data

while True:
    ret = client.publish("DEVICE_1/control", 100)
    # ( ret is retain ),( I've gave the device ID/control to control the device ) & ( 100 is the message that i gave my device to turn ON )
    
    client.loop_forever()                     # ends the statement only once as in output
    sleep(1)
   
        
# ------------------------------ OUTPUT ------------------------------ #

Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: F:\Python\Control.py ================
data published 


    
