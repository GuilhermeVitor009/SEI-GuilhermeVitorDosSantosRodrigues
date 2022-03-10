import socket #Importações de bibliotecas
import sys

TCP_IP = "127.0.0.1"
FILE_PORT = 5005 # Numero de porta do arquivo
DATA_PORT = 5006 # Numero de porta para dados
buf = 1024 # Bytes do Buffer
file_name = sys.argv[1] # Pega primeiro argumento do arquivo e guarda na variavel file_name


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ##Socket com dois argumentos= (classe do socket, tipo de entrada e saída)
    sock.connect((TCP_IP, FILE_PORT))# Conecta sockets
    sock.send(file_name)# Manda file_name para os sockets
    sock.close()# Fecha os sockets

    print "Sending %s ..." % file_name

    f = open(file_name, "rb")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##Socket com dois argumentos= (classe do socket, tipo de entrada e saída)
    sock.connect((TCP_IP, DATA_PORT)) # Conecta socket TCP_IP e DATA_PORT
    data = f.read() # Lê mensagem do arquivo
    sock.send(data) # Manda dados lidos para os sockets

finally:
    sock.close() # Fecha ligação dos sockets
    f.close() # Fecha arquivo