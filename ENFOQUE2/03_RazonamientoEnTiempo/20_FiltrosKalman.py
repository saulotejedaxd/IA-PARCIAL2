"""
20 - Filtros de Kalman
Estimacion recursiva optima para sistemas lineales gausianos.
Predice y actualiza media (mu) y varianza (sigma^2) del estado.
Aqui se implementa el caso 1D.
"""


def kalman_1d(z_obs, mu0=0.0, sigma2_0=1.0, A=1.0, H=1.0, Q=0.1, R=0.5):
    mu, sigma2 = mu0, sigma2_0
    historia = []
    for z in z_obs:
        mu_pred = A * mu
        sigma2_pred = A * sigma2 * A + Q
        K = sigma2_pred * H / (H * sigma2_pred * H + R)
        mu = mu_pred + K * (z - H * mu_pred)
        sigma2 = (1 - K * H) * sigma2_pred
        historia.append((round(mu, 3), round(sigma2, 4)))
    return historia


if __name__ == "__main__":
    medidas = [1.0, 1.2, 0.9, 1.1, 1.05, 0.95]
    print("Estimaciones (mu, sigma^2):")
    for h in kalman_1d(medidas):
        print(" ", h)
