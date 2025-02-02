import paho.mqtt.client as mqtt
import time
import random
import json
from dotenv import load_dotenv
import os
import ssl 

# Função que contém todos os dados do datasheet
def datasheet():
    solar_radiation = round(random.uniform(0, 1280), 2)
    spectral_range = round(random.uniform(300, 1100), 1)

    data = {
        "time": time.strftime("%H:%M:%S"),
        "solar_radiation": solar_radiation,
        "unit_solar_radiation": "W/m^2",
        "spectral_range": spectral_range,
        "unit_spectral_range": "nm"
    }

    return json.dumps(data)

# Carregar variáveis do .env
load_dotenv()

username = os.getenv("HIVE_USER")
password = os.getenv("HIVE_PSWD")
broker_address = os.getenv("BROKER_ADDR")

# Criação do cliente para o publisher
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")

# Configurações de TLS
client.tls_set(tls_version=ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)  # Configuração da autenticação

# Conectar ao broker
client.connect(broker_address, 8883, 60)

try:
    while True:
        message = datasheet()
        client.publish("test/topic", message, qos=1)
        
        print(f"Publicado: {message}")

        time.sleep(2)

except KeyboardInterrupt:
    print("Publicação encerrada!")

client.disconnect()
