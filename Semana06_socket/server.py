import socket  #Importações de bibliotecas
import threading
import time

SERVER_IP = socket.gethostbyname(socket.gethostname())  # função que pega o IP do servidor
PORT = 5050
ADDR = (SERVER_IP, PORT)  # Address para o server.bind
FORMATO = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  ##Servidor com dois argumentos= (classe do socket, tipo de entrada e saída)
server.bind(ADDR) #

conexoes = [] #cria lista vazia de conexões
mensagens = []  #cria lista vazia de conexões

def enviar_mensagem_individual(conexao):# Esta função manda mensagem para uma pessoa, em cada endereço a variavel conexão manda uma mensagem para o ultimo elemento da lista
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    for i in range(conexao['last'], len(mensagens)):
        mensagem_de_envio = "msg=" + mensagens[i]
        conexao['conn'].send(mensagem_de_envio.encode())
        conexao['last'] = i + 1
        time.sleep(0.2)

def enviar_mensagem_todos():
    #Nessa função ele envia para todos os clientes
    global conexoes
    for conexao in conexoes:
        enviar_mensagem_individual(conexao)

"""
1 vez que o cliente entrar, vai mandar o nome:
nome=.....
E as mensagens vem:
msg=
"""

def handle_clientes(conn, addr):
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}")
    global conexoes
    global mensagens
    nome = False

    while(True):
        msg = conn.recv(1024).decode(FORMATO)# Espera mensagem e coleta ele
        if(msg):
            if(msg.startswith("nome=")):
                mensagem_separada = msg.split("=")
                nome = mensagem_separada[1]# Apartir do momento em que eu pego o nome da mensagem, começa a conexão
                mapa_da_conexao = {
                    "conn": conn,
                    "addr": addr,
                    "nome": nome,
                    "last": 0
                }
                conexoes.append(mapa_da_conexao)# Adiciona dados na lista de conexões
                enviar_mensagem_individual(mapa_da_conexao)# Envia mensagem individual
            elif(msg.startswith("msg=")):
                mensagem_separada = msg.split("=")
                mensagem = nome + "=" + mensagem_separada[1]
                mensagens.append(mensagem)
                enviar_mensagem_todos()# Manda para todos os clientes



def start():
    print("[INICIANDO] Iniciando Socket")
    server.listen() # socket começa a ouvir o cliente
    while(True):
        conn, addr = server.accept() # Aceita a entrada de um cliente
        thread = threading.Thread(target=handle_clientes, args=(conn, addr))# Cria a thread passando dois argumentos 
        thread.start() # Começa a thread

start()