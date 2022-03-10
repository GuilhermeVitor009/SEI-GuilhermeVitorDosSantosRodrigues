import socket  #Importações das bibliotecas
import select

UDP_IP = "127.0.0.1"  #Estabelecimento do IP
IN_PORT = 5005
timeout = 3  #Valor de timeout


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)##Cria variavel da conexão de dois sockets
sock.bind((UDP_IP, IN_PORT)) # Liga duas portas

while True:
    data, addr = sock.recvfrom(1024)# Espera mensagem e coleta endereço de quem enviou
    if data:
        print "File name:", data
        file_name = data.strip()# Remove espaços da mensagem em file_name

    f = open(file_name, 'wb')#Abre arquivo

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)# Espera mensagem e coleta endereço de quem enviou
            f.write(data)# Escreve data em file_name
        else:
            print "%s Finish!" % file_name
            f.close()# Fecha arquivo
            break