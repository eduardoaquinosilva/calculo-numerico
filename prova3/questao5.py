"""
    O algoritmo aplica o modelo SIR para simular a propagação de doenças infecciosas em uma população. Esse modelo divide a população em três partes: Suscetíveis (S), Infectados (I) e Recuperados (R).

    As equações que descrevem o modelo são as seguintes:

        dS/dt = -β * SI/N
        dI/dt = β * SI/N - γI
        dR/dt = γI

    S(t): Número de indivíduos suscetíveis no tempo t.
    I(t): Número de indivíduos infectados no tempo t.
    R(t): Número de indivíduos recuperados no tempo t.
    N: População total (N = S + I + R).
    β: Taxa de transmissão.
    γ: Taxa de recuperação.
"""

import matplotlib.pyplot as plt
from numpy import linspace

N = 1000  # População total


def runge_kutta_4_sir(s0: float, i0: float, r0: float, beta: float, gamma: float, h: float, n: int):
    s, i, r = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)

    s[0], i[0], r[0] = s0, i0, r0

    for a in range(n):
        s_current, i_current, r_current = s[a], i[a], r[a]

        k1_s = -beta * s_current * i_current / N
        k1_i = beta * s_current * i_current / N - gamma * i_current
        k1_r = gamma * i_current

        k2_s = -beta * (s_current + 0.5 * h * k1_s) * (i_current + 0.5 * h * k1_i) / N
        k2_i = beta * (s_current + 0.5 * h * k1_s) * (i_current + 0.5 * h * k1_i) / N - gamma * (i_current + 0.5 * h * k1_i)
        k2_r = gamma * (i_current + 0.5 * h * k1_i)

        k3_s = -beta * (s_current + 0.5 * h * k2_s) * (i_current + 0.5 * h * k2_i) / N
        k3_i = beta * (s_current + 0.5 * h * k2_s) * (i_current + 0.5 * h * k2_i) / N - gamma * (i_current + 0.5 * h * k2_i)
        k3_r = gamma * (i_current + 0.5 * h * k2_i)

        k4_s = -beta * (s_current + h * k3_s) * (i_current + h * k3_i) / N
        k4_i = beta * (s_current + h * k3_s) * (i_current + h * k3_i) / N - gamma * (i_current + h * k3_i)
        k4_r = gamma * (i_current + h * k3_i)

        s[a + 1] = s_current + (h/6) * (k1_s + 2 * k2_s + 2 * k3_s + k4_s)
        i[a + 1] = i_current + (h/6) * (k1_i + 2 * k2_i + 2 * k3_i + k4_i)
        r[a + 1] = r_current + (h/6) * (k1_r + 2 * k2_r + 2 * k3_r + k4_r)
    
    return s, i, r


def main() -> None:
    s0 = 990
    i0 = 10
    r0 = 0
    beta = 0.3
    gamma = 0.1
    h = 0.1
    n = 1000

    s, i, r = runge_kutta_4_sir(s0, i0, r0, beta, gamma, h, n)

    t = linspace(0, n * h, n + 1)
    plt.plot(t, s, label='Suscetíveis')
    plt.plot(t, i, label='Infectados')
    plt.plot(t, r, label='Recuperados')
    
    plt.title('Modelo SIR - Método de Runge-Kutta 4ª Ordem')
    plt.xlabel('Tempo')
    plt.ylabel('Número de Indivíduos')
    
    plt.ylim(0, N)
    
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
