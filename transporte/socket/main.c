#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define PORT 8080
#define BUFFER_SIZE 1024

void sender(const char *filename) {
    int sock;
    struct sockaddr_in server_addr; // faz a estrutura para armazenar tipos de IPV4 
    char buffer[BUFFER_SIZE];
    
    // Criando o socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == -1) { // canal de comunciacao
        perror("Erro ao criar socket");
        exit(EXIT_FAILURE);
    }
    
    server_addr.sin_family = AF_INET; // define o IPV que estamos usando
    server_addr.sin_port = htons(PORT); // converte para o formato da rede 
    server_addr.sin_addr.s_addr = INADDR_ANY; // permitir que qualquer cliente se conecte ao sistema definindo o endereco
    
    // Conectar ao servidor
    if (connect(sock, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) { //
        perror("Erro ao conectar");
        exit(EXIT_FAILURE);
    }   
    
    // Abrindo o arquivo para leitura
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Erro ao abrir arquivo");
        exit(EXIT_FAILURE);
    }
    
    // Lendo até o final do arquivo e enviando os dados
    while (fgets(buffer, BUFFER_SIZE, file) != NULL) {
        send(sock, buffer, strlen(buffer), 0);
    }
    
    fclose(file);
    close(sock);
}

void receiver() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    socklen_t addr_len = sizeof(address);
    char buffer[BUFFER_SIZE];
    
    // Criando o socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("Erro ao criar socket");
        exit(EXIT_FAILURE);
    }
    
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);
    
    // Ligando o socket
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) { // associa a porta definida 
        perror("Erro ao fazer bind");
        exit(EXIT_FAILURE);
    }
    
    // Escutando conexões
    // listen(conexao, qtd_conexoes)
    if (listen(server_fd, 1) < 0) {
        perror("Erro ao escutar");
        exit(EXIT_FAILURE);
    }
    
    printf("Aguardando conexão...\n");
    
    if ((new_socket = accept(server_fd, (struct sockaddr*)&address, &addr_len)) < 0) { // aguarda a conexao com o cliente
        perror("Erro ao aceitar conexão");
        exit(EXIT_FAILURE);
    }
    
    // Recebendo os dados e exibindo
    while (1) {
        ssize_t bytes_received = recv(new_socket, buffer, BUFFER_SIZE - 1, 0); // Recebe os dados e armazena no buffer
        if (bytes_received <= 0) 
            break;
        buffer[bytes_received] = '\0';
        printf("%s", buffer);
    }
    
    printf("\n");
    close(new_socket);
    close(server_fd);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Uso: %s <sender|receiver> <arquivo>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    
    if (strcmp(argv[1], "sender") == 0) {
        sender(argv[2]);
    } else if (strcmp(argv[1], "receiver") == 0) {
        receiver();
    } else {
        fprintf(stderr, "Opção inválida. Use 'sender' ou 'receiver'.\n");
        exit(EXIT_FAILURE);
    }
    
    return 0;
}


//./socket_transfer receiver dummy.txt

//./socket_transfer sender arquivo.txt
