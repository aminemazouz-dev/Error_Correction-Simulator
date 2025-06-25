
#Sender Raspberry pi encodage RS
import socket
import random
from reedsolo import RSCodec
def canal_bruite(message, taux_erreur=0.01):
    message_bruite = bytearray()
    for byte in message:
        # Pour chaque bit dans le byte, on inverse avec une proba taux_erreur
        bits = list(f'{byte:08b}')
        for i in range(len(bits)):
            if random.random() < taux_erreur:
                bits[i] = '1' if bits[i] == '0' else '0'
        message_bruite.append(int(''.join(bits), 2))
    return bytes(message_bruite)
HOST = '192.168.100.55'  # IP de mon PC (récepteur)
PORT = 65432

message = "Test RS"  # message simple

rsc = RSCodec(32)  # 32 symboles de correction, corrige jusqu'à 16 erreurs

message_code = rsc.encode(message.encode('utf-8'))

message_bruite = canal_bruite(message_code, taux_erreur=0.01)

print("Message original :", message)
print("Message encodé RS :", message_code)
print("Message bruité    :", message_bruite)
# Envoi via socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall(message_bruite)
print("Message bruité envoyé.")
client_socket.close()
