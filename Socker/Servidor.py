from socket import *

# Configurações do servidor
servidor = "localhost"  # Endereço do servidor
porta = 5000            # Porta para escutar conexões

# Cria um socket TCP/IP
servidor_socket = socket(AF_INET, SOCK_STREAM)

# Associa o socket ao endereço e porta
servidor_socket.bind((servidor, porta))

# Escuta por conexões (até 5 clientes na fila)
servidor_socket.listen(5)
print(f"Servidor escutando em {servidor}:{porta}...")

while True:
    # Aceita uma nova conexão
    cliente_socket, endereco_cliente = servidor_socket.accept()
    print(f"Conexão estabelecida com {endereco_cliente}")

    # Recebe dados do cliente
    dados = cliente_socket.recv(1024).decode()
    print(f"Recebido: {dados}")

    # Envia uma resposta ao cliente
    resposta = "Mensagem recebida pelo servidor!"
    cliente_socket.send(resposta.encode())

    # Fecha a conexão com o cliente
    cliente_socket.close()