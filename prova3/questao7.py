import matplotlib.pyplot as plt

G = 9.81
R = 6.37e6


def euler(f: callable, v0: float, t0: float, y0: float, h: float) -> tuple[float]:
    v = []
    t = []
    y = []

    while y0 >= 0:
        v.append(v0)
        t.append(t0)
        y.append(y0)

        v0 += h * f(t0, y0)
        y0 += v0 * h
        t0 += h

    return t, v, y


def f(t, x):
    return -G * R**2 / (R + x)**2


def main():
    t0 = 0
    v0 = 1400
    y0 = 0
    h = 0.1

    t_euler, v_euler, y_euler = euler(f, v0, t0, y0, h)

    print("Altura máxima:", max(y_euler))

    plt.plot(t_euler, v_euler, color='g', label='Velocidade', linestyle=':')
    plt.plot(t_euler, y_euler, color='purple', label='Posição', linestyle='-.')
    
    plt.title('Velocidade / Distância vs Tempo')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s) / Distância (m)')
    
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
