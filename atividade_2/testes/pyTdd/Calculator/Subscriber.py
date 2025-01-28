import paho.mqtt.client as mqtt

class MQTTSubscriber:
    def __init__(self, broker_address, port, topic, client_id="python_subscriber"):
        self.broker_address = broker_address
        self.port = port
        self.topic = topic
        self.client_id = client_id
        self.recived = []

        # Configuração do cliente
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, reason_code, properties=None):
        if reason_code == 0:
            print("Conexão bem sucedida!")
            client.subscribe(self.topic, 1)
        else:
            print(f"Conexão falhou! Código {reason_code}")
            exit(reason_code)

    def on_message(self, client, userdata, message):
        msg = message.payload.decode()
        self.recived.append(msg)
        print(f"Recebido: {msg} no tópico {message.topic}")
        client.disconnect()

    def start(self):
        self.client.connect(self.broker_address, self.port, 60)
        self.client.loop_forever()

    # Método para retornar as mensagens recebidas
    def get_received(self):
        return self.recived
