import socket

# Configuração do servidor
HOST = "127.0.0.1"  # Localhost
PORT = 12345        # Porta de escuta

# Criar o socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Servidor UDP rodando em {HOST}:{PORT}")

while True:
    data, client_address = server_socket.recvfrom(1024)  # Receber mensagem (até 1024 bytes)
    print(f"Mensagem recebida de {client_address}: {data.decode()}")
    
    # Responder ao cliente
    response = "Mensagem recebida com sucesso!"
    server_socket.sendto(response.encode(), client_address)
