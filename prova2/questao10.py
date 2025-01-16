from scipy.interpolate import CubicSpline

X = 0.25


def main() -> None:
    # Pontos de amostra
    T = [(0, 3), (0.5, 1.8616), (1, -0.5571), (1.5, -4.1987), (2, -9.0536)]

    # Separa os pontos em coordenadas x e y
    x_points, y_points = zip(*T)

    # Cria a spline cúbica com os pontos fornecidos
    spline = CubicSpline(x_points, y_points)

    # Exibe o valor interpolado em X
    print(f"Valor interpolado em x = {X}: {spline(X):.4f}")


if __name__ == '__main__':
    main()
