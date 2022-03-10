import socket #Importações de biblioteca socket

TCP_IP = "127.0.0.1"
FILE_PORT = 5005 # Numero de porta do arquivo
DATA_PORT = 5006 # Numero de porta para dados
buf = 1024 # Bytes do Buffer
timeout = 3


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##Cria variavel da conexão de dois sockets
sock_f.bind((TCP_IP, FILE_PORT)) # Liga duas portas
sock_f.listen(1) # socket ouve a porta 1

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##Cria variavel da conexão de dois sockets
sock_d.bind((TCP_IP, DATA_PORT))# Liga duas portas
sock_d.listen(1)# socket ouve a porta 1


while True:
    conn, addr = sock_f.accept()# Aceita a entrada de um socket
    data = conn.recv(buf)# Variavel que verifica se arquivo foi enviado
    if data: # Se isso acontece
        print "File name:", data
        file_name = data.strip()# Remove espaços da mensagem em file_name

    f = open(file_name, 'wb')# Abre arquivo

    conn, addr = sock_d.accept() # Aceita a entrada de um socket
    while True:
        data = conn.recv(buf)
        if not data:
            break
        f.write(data) # Escreve dados no arquivo

    print "%s Finish!" % file_name
    f.close() # fecha arquivo