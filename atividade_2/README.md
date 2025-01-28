Esse projeto tem por objetivo utilizar a base feita na atividade_1 desse repositório em que foi criado um publisher. 
Nesse sentido, foi feito agora um processo de TDD para realizar os testes no código. Além disso, foi utilizado sistema de QoS para questões de qualidade de serviço.

# Execução do projeto
1 - Para executar esse sistema primeiramente você necessita clonar o repositório da atividade_1 e esse respositório (atividade_2).

2 - Na sua máquina você precisa ter um arquivo chamado `mosquitto.conf` que terá a seguinte configuração:

```
listener 1891
allow_anonymous truelistener 1891
allow_anonymous true
```

3 - Execute agora em um terminal o comando `mosquitto -c mosquitto.conf`

4 - Após isso inicie uma máquina virtual, através do comando `python3 -m venv venv` e inicie com `. venv/bin/activate` no terminal integrado do VS Code.

5 - Agora vá na `atividade_1` e execute `python3 publisher.py`

6 - Agora vá para a `atividade_2` e execute `pytest` 


Os testes realizados foram feitos se estava chegando agluma mensgaem pelo tópico; se a mensagem continha dados válidos (ou seja, nesse caso se possuia os campos de 'time', 'solar_radiation', 'unit_solar_radiation', 'spectral_range' e 'unit_spectral_range'); foi feito também o teste para analisar o teste de disparo e também teste com o QoS para qualidade.

Nesse sentido, o teste de QoS está englobado no de disparo, pois foi inserido na classe em que se adapta o subscriber (caminho: [atividade_2/testes/pyTdd/Calculator/Subscriber.py](testes/pyTdd/Calculator/Subscriber.py)) o QoS e a partir do tempo se valda esse teste de qualidade.