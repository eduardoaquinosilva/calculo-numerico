from questao3 import gaussian_elimination

def main() -> None:
    solutions_matrix_1 = gaussian_elimination(
        [[1, -1],
         [1, -1.00001]], [1, 0]
    )

    solutions_matrix_2 = gaussian_elimination(
        [[1, -1],
         [1, -0.99999]], [1, 0]
    )

    print(f"Solução do primeiro sistema (x, y): ({solutions_matrix_1[0]}, {solutions_matrix_1[1]}).")
    print(f"Solução do segundo sistema (x, y): ({solutions_matrix_2[0]}, {solutions_matrix_2[1]}).")


if __name__ == '__main__':
    main()
