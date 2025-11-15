# Importa o módulo socket
from socket import *
import sys  # Necessário para encerrar o programa

# Cria o socket TCP (orientado à conexão)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket do servidor

# Fill in start
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# Fill in end

while True:
    # Estabelece a conexão
    print('Ready to serve...')
    connectionSocket, addr = (
        # Fill in start
        serverSocket.accept())
    # Fill in end

    try:
        # Recebe a mensagem do cliente (requisição HTTP)
        message = (
            # Fill in start
            connectionSocket.recv(1024).decode())
        # Fill in end

        # Caso a requisição venha vazia, evita crash
        if len(message) < 1:
            connectionSocket.close()
            continue

        filename = message.split()[1]

        # Abre o arquivo solicitado com encoding seguro
        f = open(filename[1:], encoding="utf-8")
        outputdata = (
            # Fill in start
            f.read())
        # Fill in end

        # Envia o cabeçalho HTTP 200 OK
        # Fill in start
        connectionSocket.send(
            "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n".encode())
        # Fill in end

        # Envia o conteúdo do arquivo ao cliente
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Fecha a conexão com o cliente
        connectionSocket.close()

    except IOError:
        # Envia mensagem de erro 404 se o arquivo não for encontrado
        # Fill in start
        connectionSocket.send(
            "HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n".encode())

        f = open("404.html", encoding="utf-8")
        error_page = f.read()
        connectionSocket.send(error_page.encode())
        # Fill in end

        # Fecha o socket do cliente
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  # Encerra o programa
