import socket #Importações de bibliotecas
import threading
import time

PORT = 5050
FORMATO = 'utf-8'
SERVER = "192.168.0.109"  # IP do servidor
ADDR = (SERVER, PORT)  # Address para o server.bind

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ##Cliente com dois argumentos= (classe do socket, tipo de entrada e saída)
client.connect(ADDR)  # Conexão no ADDR

def handle_mensagens():
    while(True):
        msg = client.recv(1024).decode()# Aqui pega o tamanho maximo da mensagem
        mensagem_splitada = msg.split("=")# Divide a mensagem em uma lista com mensagens separadas
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])

def enviar(mensagem):
    client.send(mensagem.encode(FORMATO))# Envia a mensagem

def enviar_mensagem():
    mensagem = input()
    enviar("msg=" + mensagem)

def enviar_nome():
    nome = input('Digite seu nome: ')
    enviar("nome=" + nome)

def iniciar_envio():
    enviar_nome()
    enviar_mensagem()

def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)# Duas threads vão rodar
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()#começa as threads
    thread2.start()

iniciar() # Inicia as threads de mensagens e de envio