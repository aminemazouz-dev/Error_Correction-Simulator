#Sender Raspberry Pi
import random
import socket

def canal_bruite(message, taux_erreur=0.1):
    message_bruite = ""
    for bit in message:
        if random.random() < taux_erreur:
            # Inverse le bit (0 -> 1, 1 -> 0)
            message_bruite += '1' if bit == '0' else '0'
        else:
            message_bruite += bit
    return message_bruite

HOST = '192.168.100.55'  # IP locale de mon PC (receiver)
PORT = 65432

message = "101101011001"  # Message binaire exemple

# Appliquer le canal bruité avec un taux d'erreur de 10%
message_bruite = canal_bruite(message, taux_erreur=0.1)

print("Message original :", message)
print("Message bruité   :", message_bruite)

# Création du socket client (sender)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Envoi du message bruité
client_socket.sendall(message_bruite.encode())

print("Message bruité envoyé.")

client_socket.close()
