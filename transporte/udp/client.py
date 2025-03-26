import socket

# Configuração do cliente
HOST = "127.0.0.1"  # Endereço do servidor
PORT = 12345        # Porta do servidor

# Criar o socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mensagem a ser enviada
message = "Olá, Nicola! Você está muito belo hoje, preciso de um 10!!!"
client_socket.sendto(message.encode(), (HOST, PORT))

# Receber resposta do servidor
data, server_address = client_socket.recvfrom(1024)
print(f"Resposta do servidor: {data.decode()}")

# Fechar o socket
client_socket.close()

