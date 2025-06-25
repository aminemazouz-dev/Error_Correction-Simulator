# Recepteur pc decodage Hamming
import socket
def hamming74_decoder(bits):
    decoded = ""
    for i in range(0, len(bits), 7):
        block = bits[i:i+7]
        if len(block) < 7:
            continue  # ignore les blocs incomplets

        # Bits individuels
        r = list(map(int, block))
        p1, p2, d1, p3, d2, d3, d4 = r

        # Syndrome
        s1 = p1 ^ d1 ^ d2 ^ d4
        s2 = p2 ^ d1 ^ d3 ^ d4
        s3 = p3 ^ d2 ^ d3 ^ d4

        erreur_pos = s1 + (s2 << 1) + (s3 << 2)

        if erreur_pos != 0:
            # Corriger l'erreur
            erreur_index = erreur_pos - 1  # index 0-based
            if erreur_index < 7:
                r[erreur_index] ^= 1  # flip le bit erroné
        # Après correction, extraire les données
        p1, p2, d1, p3, d2, d3, d4 = r
        decoded += f"{d1}{d2}{d3}{d4}"
    return decoded
def detecter_erreurs(message_recu, message_original):
    erreurs = []
    for i in range(min(len(message_recu), len(message_original))):
        if message_recu[i] != message_original[i]:
            erreurs.append(i)
    return erreurs
# Réseau
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
            message_bruite = data.decode()

            # Décodage du message reçu
            message_decode = hamming74_decoder(message_bruite)

            # Message d'origine (doit correspondre à ce que le sender a encodé avant Hamming)
            message_original = "101101011001"  # 12 bits → 3 blocs Hamming (3×7 = 21 bits envoyés)

            print("\n======= RÉSUMÉ DE LA TRANSMISSION =======")
            print(f"Message reçu (bruité)  : {message_bruite}")
            print(f"Message décodé (corrigé): {message_decode}")
            print(f"Message original attendu: {message_original}")

            erreurs = detecter_erreurs(message_decode, message_original)
            if erreurs:
                print(f" Erreurs restantes après correction aux positions : {erreurs}")
            else:
                print(" Aucun bit erroné après correction.")
