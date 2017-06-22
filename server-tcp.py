# -*- coding:utf-8 -*-

# Servidor básico para conexões TCP 

# Importando as bibliotecas

import socket
import thread


bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

server.bind ((bind_ip, bind_port ))

# Atraso máximo de 5 segundos

server.listen (5)

print " [*] Ouvindo na porta  % s:% d" % (bind_ip, bind_port)

# Segmento para o tratamento do cliente

def handle_client (client_socket):

	# Imprimir o que o cliente envia
	request = client_socket.recv (1024)

	print " [*] recebida : % s " % (request)

# Envia um pacote de volta

client_socket.send ( " ACK !")

client_socket.close ()


while True:

	client, addr = server.accept ()

	print " [*] Conexão aceita a partir de:% s:% d" % (addr [0], addr [1] )

	client_handler = threading.Thread (target = handle_client, args = (client,))
	client_handler.start()
