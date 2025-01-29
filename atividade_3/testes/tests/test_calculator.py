from pyTdd.Calculator import Operations
from pyTdd.Calculator.Subscriber import MQTTSubscriber as Subscriber
import paho.mqtt.client as mqtt
import time
import os

broker_address = os.getenv("BROKER_ADDR")

def test_adder():
    adder = Operations.Adder()
    assert adder.Add(1, 2, 3) == 6

def test_adder1():
    adder = Operations.Adder()
    # assert 1 + 2 == 3 and 2+2 == 4
    # assert adder.Add(1, 2, 3) == 6

# Validacao de tempo de disparo
def tempo_disparo(start, end):
    assert (end - start) <= 5.0


# Valida se a mensagem veio no formato correto
def validacao(message):
    # print(f'O tipo da mensagem é {(message)}')
    dados_validos = ['time', 'solar_radiation', 'unit_solar_radiation', 'spectral_range', 'unit_spectral_range']
    for dados in dados_validos:

        assert dados in message[0]

# Encapsulamento da classe para fazer o subscriber
subscriber = Subscriber(broker_address = broker_address, port=8883, topic="test/topic")


start_time = time.time()
# inicia o subscriber
subscriber.start()
print(subscriber.get_received())
end_time = time.time()

tempo_disparo(start_time, end_time)

assert len(subscriber.get_received()) > 0

validacao(subscriber.get_received())



