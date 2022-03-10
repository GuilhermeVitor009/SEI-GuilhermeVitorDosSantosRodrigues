import socket  #Importações de bibliotecas
import time
import sys

TCP_IP = "127.0.0.1"
FILE_PORT = 5005 # Numero de porta do arquivo
buf = 1024 # Bytes do Buffer
file_name = sys.argv[1] # Pega primeiro argumento do arquivo e guarda na variavel file_name


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)##Cria variavel da conexão de dois sockets
sock.sendto(file_name, (UDP_IP, UDP_PORT))# Manda arquivo no primeiro argumento para segundo argumento
print "Sending %s ..." % file_name

f = open(file_name, "r")# Abre arquivo
data = f.read(buf)
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        data = f.read(buf)# lê arquivo com 1024 bytes de transmissão
        time.sleep(0.02) # Give receiver a bit time to save

sock.close() # Fecha ligação de sockets
f.close()# Fecha arquivo
