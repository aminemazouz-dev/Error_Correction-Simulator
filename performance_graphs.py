# Graphe Comparaison Performance
import numpy as np
import plotly.graph_objects as go
from reedsolo import RSCodec, ReedSolomonError
def simulate_hamming(error_rate, trials=100):
    def hamming_encode(msg):
        G = np.array([
            [1, 0, 0, 0, 0, 1, 1],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1]
        ])
        return np.dot(msg, G) % 2
    def hamming_decode(code):
        H = np.array([
            [0, 0, 0, 1, 1, 1, 1],
            [0, 1, 1, 0, 0, 1, 1],
            [1, 0, 1, 0, 1, 0, 1]
        ])
        syndrome = np.dot(H, code) % 2
        syndrome_decimal = int(''.join(str(int(x)) for x in syndrome[::-1]), 2)
        if syndrome_decimal != 0:
            code[syndrome_decimal - 1] ^= 1
        return code[:4]
    success_count = 0
    for _ in range(trials):
        msg = np.random.randint(0, 2, 4)
        encoded = hamming_encode(msg)
        noisy = encoded.copy()
        if np.random.rand() < error_rate:
            pos = np.random.randint(0, 7)
            noisy[pos] ^= 1
        decoded = hamming_decode(noisy)
        if np.array_equal(decoded, msg):
            success_count += 1
    return success_count / trials * 100

def simulate_rs(message_bytes, error_rate, nsym=32):
    rsc = RSCodec(nsym)
    encoded = rsc.encode(message_bytes)
    n_errors = int(len(encoded) * error_rate)
    noisy = bytearray(encoded)
    error_positions = np.random.choice(len(encoded), n_errors, replace=False)
    for pos in error_positions:
        noisy[pos] ^= np.random.randint(1, 256)
    try:
        rsc.decode(noisy)
        return 1.0
    except ReedSolomonError:
        return 0.0

def get_avg_rs_correction_rate(message, error_rate, trials=20):
    return np.mean([simulate_rs(message, error_rate) for _ in range(trials)]) * 100

# Simulation
error_rates = np.linspace(0, 0.5, 15)
rs_results = [get_avg_rs_correction_rate(b'Test RS', e) for e in error_rates]
hamming_results = [simulate_hamming(e) for e in error_rates]

# Graphique
fig = go.Figure()

fig.add_trace(go.Scatter(x=error_rates*100, y=rs_results,
                         mode='lines+markers',
                         name='Reed-Solomon',
                         line=dict(color='royalblue', width=3)))

fig.add_trace(go.Scatter(x=error_rates*100, y=hamming_results,
                         mode='lines+markers',
                         name='Hamming (7,4)',
                         line=dict(color='firebrick', width=3)))

fig.update_layout(
    title='Comparaison des taux de correction : Hamming vs Reed-Solomon',
    xaxis_title='Taux d\'erreur injecté (%)',
    yaxis_title='Taux de correction obtenu (%)',
    xaxis=dict(range=[0, 50]),
    yaxis=dict(range=[0, 105]),
    template='plotly_white'
)

fig.show()
