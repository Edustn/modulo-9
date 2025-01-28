import paho.mqtt.client as mqtt
import time
import random
import json

# Função que contém todos os dados do datashet

def datasheet():
    solar_radiation = round(random.uniform(0,1280), 2)
    spectral_range = round(random.uniform(300, 1100), 1)
    
    data = {
        "time": time.strftime("%H:%M:%S"),
        "solar_radiation": solar_radiation,
        "unit_solar_radiation": "W/m^2",

        "spectral_range": spectral_range,
        "unit_spectral_range": "nm"


    }
    
    return json.dumps(data)
    
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

