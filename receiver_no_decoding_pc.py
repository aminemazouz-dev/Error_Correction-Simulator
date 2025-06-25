# Recepteur pc
import socket
def detecter_erreurs(message_recu, message_original):
    erreurs = []
    for i in range(len(message_original)):
        if message_recu[i] != message_original[i]:
            erreurs.append(i)
    return erreurs
HOST = '0.0.0.0'  # écoute sur toutes les interfaces
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
            message_recu = data.decode()
            message_original = "101101011001"  # Exemple

            print(f"Message reçu :       {message_recu}")
            print(f"Message original :   {message_original}")

            erreurs = detecter_erreurs(message_recu, message_original)
            if erreurs:
                print(f"Erreurs détectées aux positions : {erreurs}")
            else:
                print("Aucune erreur détectée.")
