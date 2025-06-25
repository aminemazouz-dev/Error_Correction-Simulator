# Recepteur RS PC
import socket
from reedsolo import RSCodec

rsc = RSCodec(32)  # même configuration qu’au sender

def decoder_message(message_bytes):
    try:
        decoded_tuple = rsc.decode(message_bytes)
        # decode() retourne un tuple (message_corrige, erreurs_detectees)
        message_decode = decoded_tuple[0]
        return message_decode.decode('utf-8')
    except Exception as e:
        return f"[Erreur lors du décodage] : {e}"

HOST = '0.0.0.0'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("En attente de connexion...")
    conn, addr = s.accept()
    with conn:
        print(f"Connecté par {addr}")
        data = conn.recv(1024)
        if not data:
            print("Pas de données reçues.")
        else:
            print("Message reçu (bytes) :", data)
            message_corrige = decoder_message(data)
            print("Message après correction :", message_corrige)
