# -*- coding:utf-8 -*-

# Cliente básico em python , para conexões TCP
# Run on python 2.7
# Author Victor Consuegra 
# wolfsecurity@protonmail.com

# Principais módulos 

import socket  

target_host = "0.0.0.0"

target_port = 9999

# Este será o socket

client = socket.socket ( socket.AF_INET, socket.SOCK_STREAM)

# Estabelecer conexão com o servidor

client.connect ((target_host, target_port))

# Envia os dados para o servidor após a conexão

client.send ( "GET / HTTP / 1.1 \ r \ nHost: 0.0.0.0 r \ n \ r \ n \ ")

# Receber dados

resposta = client.recv ( 4096 )

print resposta
