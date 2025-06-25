# Sender Raspberry Pi avec Encodage Hamming (7,4)
import random
import socket
# Fonction d'encodage Hamming(7,4)
def hamming_encode(data_4bits):
    d = list(map(int, data_4bits))
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    encoded = [p1, p2, d[0], p3, d[1], d[2], d[3]]
    return ''.join(str(bit) for bit in encoded)
# Canal bruité
def canal_bruite(message, taux_erreur=0.1):
    message_bruite = ""
    for bit in message:
        if random.random() < taux_erreur:
            message_bruite += '1' if bit == '0' else '0'
        else:
            message_bruite += bit
    return message_bruite

# Configuration
HOST = '192.168.100.55'  # IP du récepteur
PORT = 65432
message_original = "101101011001"  # 12 bits

# Étape 1 : Diviser le message en blocs de 4 bits
blocs_4bits = [message_original[i:i+4] for i in range(0, len(message_original), 4)]

# Étape 2 : Encoder chaque bloc avec Hamming(7,4)
message_encode = ''.join(hamming_encode(bloc) for bloc in blocs_4bits)

# Étape 3 : Ajouter du bruit
message_bruite = canal_bruite(message_encode, taux_erreur=0.1)

# Affichage
print("Message original   :", message_original)
print("Message encodé     :", message_encode)
print("Message bruité     :", message_bruite)

# Étape 4 : Envoi
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall(message_bruite.encode())
print("Message bruité envoyé.")
client_socket.close()
