Esse projeto foi feito para integração entre a `atividade_1` e `atividade_2` com broker Hivemq. Nesse sentido, pode-se ter os testes realizados e a integração do sistema.


# Execução do projeto
1 - Para executar esse sistema primeiramente você necessita clonar o repositório da `atividade_3`

2 - Após isso inicie uma máquina virtual, através do comando `python3 -m venv venv` e inicie com `. venv/bin/activate` no terminal integrado do VS Code.

3 - Execute o comando `pip install -r requirements.txt`

4 - Crie na pasta `atividade_3` um arquivo .env e preencha com os seus dados do Hivemq:

```
BROKER_ADDR = ''
HIVE_USER = ''
HIVE_PSWD = ''
```

5 - Agora vá na `atividade_3/testes` e execute `python3 publisher.py`

6 - Agora execute o comando `pytest` para ver os resultados do teste e se está conectando com seu broker.


Vídeo de demonstração: [https://drive.google.com/file/d/1Y22aBQW0fJGbr2LPmBAieDusu2pT0D9r/view?usp=sharing](https://drive.google.com/file/d/1Y22aBQW0fJGbr2LPmBAieDusu2pT0D9r/view?usp=sharing)
