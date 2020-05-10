import paho.mqtt.client as mqtt 

broker= "117.170.84.60"                  # This is my broker IP
port = 18879                             # This is my Broker Port number

def on_connect(client, userdata, flags, rc):               # create bind to call back
    if rc==0:
        print("connected OK")
        global connection
        connection = True                # Set Flag
    else:
        print(" 'Bad connection' Returned code = ",rc)
        
# call back        
        
connection = False                       # create flag in class
client = mqtt.Client("MQTT")             # create new instance 
client.on_connect=on_connect             # bind call back function
client.loop_start()
print("Connecting to broker ",broker,port)
client.connect(broker, port) 



# --- OUTPUT --- #
    
Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========================= RESTART: F:/python/method1.py ========================
Connecting to broker  117.170.84.60 18879
>>> connected OK    
