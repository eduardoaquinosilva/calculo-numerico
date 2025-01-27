import matplotlib.pyplot as plt

G = 9.81
CD = 0.225
M = 90


def euler(f: callable, v0: float, t0: float, y0: float, h: float) -> tuple[float]:
    v = []
    t = []
    y = []

    while y0 > 0:
        v.append(v0)
        t.append(t0)
        y.append(y0)

        v0 += h * f(t0, v0)
        y0 -= v0 * h
        t0 += h

    return t, v, y


def runge_kutta_4(f: callable, v0: float, t0: float, y0: float, h: float) -> tuple[float]:
    v = []
    t = []
    y = []
    
    while y0 > 0:
        v.append(v0)
        t.append(t0)
        y.append(y0)

        k1_v = f(t0, v0)
        k1_y = v0

        k2_v = f(t0 + h / 2, v0 + h / 2 * k1_v)
        k2_y = v0 + h / 2 * k1_y

        k3_v = f(t0 + h / 2, v0 + h / 2 * k2_v)
        k3_y = v0 + h / 2 * k2_y

        k4_v = f(t0 + h, v0 + h * k3_v)
        k4_y = v0 + h * k3_y

        v0 += (h / 6) * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)
        y0 -= (h / 6) * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)
        t0 += h
        
    return t, v, y


def f(t, v):
    return G - (CD / M) * v**2


def main():
    t0 = 0
    v0 = 0
    y0 = 1000
    h = 0.1

    t_rk4, v_rk4, y_rk4 = runge_kutta_4(f, v0, t0, y0, h)
    t_euler, v_euler, y_euler = euler(f, v0, t0, y0, h)

    plt.plot(t_rk4, v_rk4, color='r', label='Runge Kutta 4 - Velocidade')
    plt.plot(t_euler, v_euler, color='g', label='Euler - Velocidade', linestyle=':')
    plt.plot(t_rk4, y_rk4, color='b', label='Runge Kutta 4 - Posição', linestyle='--')
    plt.plot(t_euler, y_euler, color='purple', label='Euler - Posição', linestyle='-.')
    
    plt.title('Velocidade / Distância vs Tempo')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s) / Distância (m)')
    
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
