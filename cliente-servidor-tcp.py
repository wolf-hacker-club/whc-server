#!/usr/bin/python
# -*- coding: iso8859-1 -*-

"""
Este script serve para exemplificar o uso de sockets em python para o trafego de dados em rede.
É bem simples, nele estão definidos o servidor e o clinete (que são habilitados de acordo com os argumentos durante a chamada na linha de comando.

Exemplo:

$ ./sockets.py -s 9099      # Isso em um terminal

$ ./sockets.py -c localhost 9099        # Em outro terminal

"""


""" Módulo necessário para utilização de sockets"""
from socket import *

""" Módulos para receber argumentos via linha de comando e sair do programa (exit) """
from sys import argv,exit

def conecta(ip,porta):
    """ Esta função recebe um ip e uma porta e faz a conexão"""

    sock = socket(AF_INET,SOCK_STREAM) # Criação do socket
    sock.connect((ip,int(porta))) # Conexão com o servidor
    return sock

def server():
    """ Esta função abre um servidor que fica esperando por conexões de rede na porta definida. """
    NUMERO_CONEXOES = 1 # Número de conexões que o server aceitara

    if len(argv) < 3:
        usage()
        exit(1)

    sock = socket(AF_INET,SOCK_STREAM)  #   Criação do socket do servidor
    sock.bind(("localhost",int(argv[2])))   #   Faz o socket escutar no ip "localhost" e porta passado no argumento
    sock.listen(NUMERO_CONEXOES)    #   Escuta até NUMERO_CONEXOES conexões
    client = sock.accept()  #   Aceita e espera por conexões
    new_sock = client[0]    #   client[0] contém o socket para a conexão aberta,
    ip = client[1][0] # client[1] contém uma tupla com informações sobre o client no formato (ip,porta)
    print "Cliente conectado.\nInformações:\n\tIP: %s" % ip
    print "O Server está de pé, esperando por mensagens. CTRL+C para derrubar o server.\n"
    BY = 1024
    try:
        msg = True
        while msg != None:
            msg = new_sock.recv(BY)   #   Recebe uma mensagem pelo socket aberto, recebe até BY bytes
            print "Mensagem recebida de %s -> %s" % (ip,msg)
    except KeyboardInterrupt:   #   Trata o CTRL+C
        print "Saindo..."
        exit(0)

def client():
    """ Função que representa o cliente, conecta no servidor e interage com o usuário """
    if len(argv) < 4:
        usage()
        exit(1)
    sock = conecta(argv[2],argv[3]) #   Conecta
    try:
        while True:
            msg = raw_input("Digite sua mensagem (para sair pressione ctrl+c): ")
            sock.send(msg)  # Envia a mensagem

    except KeyboardInterrupt:   #   Trata o CTRL+C
        sock.send("{FONTE}")
        print "Saindo..."
        exit(0)

def usage():
    print "Uso: %s options [ip] [porta]\n\n\t-s abre o programa como servidor, especifique a porta\n\t-c abre o programa como client, especifique o ip e a porta" % argv[0]


if __name__ == "__main__":
    args = ("-s","-c","-h")
    if len(argv) < 2 or argv[1] not in args or argv[1] == "-h":
        usage()
        exit(1)

    if argv[1] == args[0]:
        print "Executando o server.\n"
        server()

    elif argv[1] == args[1]:
        print "Executando o cliente.\n"
        client()

    exit(0)