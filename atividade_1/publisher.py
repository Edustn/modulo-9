import paho.mqtt.client as mqtt
import time
import random

# Função que contém todos os dados do datashet

def datasheet():
    
    return {
        "time": time.strftime("%H:%M:%S"),

    }

# Criação do cliente para o publisher

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")
client.connect("localhost", 1891, 60)

try: 
    while True:
        message = "" + (str(datasheet()))
        client.publish("test/topic", message)
        print(f"Publicado: {message}")

        time.sleep(2)

except KeyboardInterrupt: 
    print("Publicação encerrada!")

client.disconnect()

