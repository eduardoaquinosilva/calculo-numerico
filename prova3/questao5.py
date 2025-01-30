"""
    O algoritmo aplica o modelo SIR para simular a propagação de um vírus em uma rede de computadores.
    
    Uma empresa possui uma rede de computadores interconectados. Em determinado momento, um vírus começa a se espalhar pela rede através de e-mails infectados e compartilhamento de arquivos.

    Esse modelo divide as máquinas em quatro categorias: Suscetíveis (S), Infectados (I), Removidos (R) e Protegidos (P).

    As equações que descrevem o modelo são as seguintes:

        dS/dt = -βSI - αSP
        dI/dt = βSI - γI
        dR/dt = γI
        dP/dt = αSP

    S(t): Computadores que ainda não foram infectados, mas podem ser.
    I(t): Computadores que foram infectados e estão propagando o vírus.
    R(t): Computadores que foram limpos ou formatados e não podem mais ser infectados.
    P(t): Computadores que possuem um antivírus atualizado e não podem ser infectados.
    N: Total de máquinas (N = S + I + R + P).
    β: Taxa de infecção do vírus através da interação entre computadores suscetíveis e infectados.
    α: Taxa de proteção, ou seja, a taxa com que computadores suscetíveis instalam um antivírus e se tornam protegidos.
    γ: Taxa de recuperação, isto é, a taxa com que computadores infectados são formatados ou limpos e passam para a categoria de removidos.
"""

import matplotlib.pyplot as plt
from numpy import linspace

N = 1000  # População total


def dSdt(s: float, i: float, p: float, beta: float, alpha: float) -> float:
    return -beta * s * i - alpha * s * p


def dIdt(s: float, i: float, p: float, beta: float, gamma: float) -> float:
    return beta * s * i - gamma * i


def dRdt(i: float, gamma: float) -> float:
    return gamma * i


def dPdt(s: float, p: float, alpha: float) -> float:
    return alpha * s * p


def runge_kutta_4_sir(s0: float, i0: float, r0: float, p0: float, beta: float, alpha: float, gamma: float, h: float, n: int) -> tuple[list[float]]:
    steps = int(n / h)

    s, i, r, p, total = [0] * steps, [0] * steps, [0] * steps, [0] * steps, [0] * steps
    t = linspace(0, n, steps)

    s[0], i[0], r[0], p[0], total[0] = s0, i0, r0, p0, s0 + i0 + r0 + p0

    for a in range(steps - 1):
        k1_s = h * dSdt(s[a], i[a], p[a], beta, alpha)
        k1_i = h * dIdt(s[a], i[a], p[a], beta, gamma)
        k1_r = h * dRdt(i[a], gamma)
        k1_p = h * dPdt(s[a], p[a], alpha)

        k2_s = h * dSdt(s[a] + k1_s/2, i[a] + k1_i/2, p[a] + k1_p/2, beta, alpha)
        k2_i = h * dIdt(s[a] + k1_s/2, i[a] + k1_i/2, p[a] + k1_p/2, beta, gamma)
        k2_r = h * dRdt(i[a] + k1_i/2, gamma)
        k2_p = h * dPdt(s[a] + k1_s/2, p[a] + k1_p/2, alpha)

        k3_s = h * dSdt(s[a] + k2_s/2, i[a] + k2_i/2, p[a] + k2_p/2, beta, alpha)
        k3_i = h * dIdt(s[a] + k2_s/2, i[a] + k2_i/2, p[a] + k2_p/2, beta, gamma)
        k3_r = h * dRdt(i[a] + k2_i/2, gamma)
        k3_p = h * dPdt(s[a] + k2_s/2, p[a] + k2_p/2, alpha)

        k4_s = h * dSdt(s[a] + k3_s, i[a] + k3_i, p[a] + k3_p, beta, alpha)
        k4_i = h * dIdt(s[a] + k3_s, i[a] + k3_i, p[a] + k3_p, beta, gamma)
        k4_r = h * dRdt(i[a] + k3_i, gamma)
        k4_p = h * dPdt(s[a] + k3_s, p[a] + k3_p, alpha)

        s[a + 1] = s[a] + (k1_s + 2*k2_s + 2*k3_s + k4_s) / 6
        i[a + 1] = i[a] + (k1_i + 2*k2_i + 2*k3_i + k4_i) / 6
        r[a + 1] = r[a] + (k1_r + 2*k2_r + 2*k3_r + k4_r) / 6
        p[a + 1] = p[a] + (k1_p + 2*k2_p + 2*k3_p + k4_p) / 6
        total[a + 1] = s[a + 1] + i[a + 1] + r[a + 1] + p[a + 1]

    return s, i, r, p, t, total


def main() -> None:
    i0 = 10
    r0 = 0
    p0 = 200
    s0 = N - i0 - r0 - p0
    beta = 0.002
    alpha = 0.001
    gamma = 0.1
    h = 0.1
    n = 50

    s, i, r, p, t, total = runge_kutta_4_sir(s0, i0, r0, p0, beta, alpha, gamma, h, n)

    plt.figure(figsize=(10,6))
    plt.plot(t, s, label='Suscetíveis')
    plt.plot(t, i, label='Infectados')
    plt.plot(t, r, label='Removidos')
    plt.plot(t, p, label='Protegidos')
    plt.plot(t, total, label='Total de Computadores')
    
    plt.title('Modelo SIR - Propagação de um Vírus em uma Rede de Computadores')
    plt.xlabel('Tempo (dias)')
    plt.ylabel('Número de Computadores')
    
    plt.ylim(0, N + 10)
    
    plt.grid()
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
