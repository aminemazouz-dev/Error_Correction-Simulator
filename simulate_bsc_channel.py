# Simulation Canal BSC
import numpy as np

# Paramètres
n = 8               # Longueur du message
p = 0.2             # Probabilité d'erreur sur chaque bit

# Génération du message original (binaire aléatoire)
M = np.random.randint(0, 2, n)

# Application du bruit (canal binaire symétrique)
E = np.random.rand(n) < p       # Tableau booléen : True si erreur sur le bit
M_bruite = M ^ E.astype(int)    # XOR bit à bit pour inverser les bits erronés

# Recherche des positions des erreurs (indices +1 pour correspondre à la numérotation humaine)
positions_erreurs = np.where(E)[0] + 1

# Affichage des résultats
print(f"Message original : {M}")
print(f"Message reçu     : {M_bruite}")
print(f"Positions des erreurs : {set(positions_erreurs)}")

