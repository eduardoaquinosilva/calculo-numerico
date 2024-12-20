from numpy import linalg
from questao3 import gaussian_elimination

N = 10

def get_hilbert_matrix(size: int) -> list[list[float]]:
    maxtrix = [[] for _ in range(size)]
    
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            x = 1 / (i + j - 1)
            maxtrix[i - 1].append(x)

    return maxtrix


def main() -> None:
    hilbert_matrices = [get_hilbert_matrix(n) for n in range(1, N + 1)]
    condition_numbers = [linalg.cond(h) for h in hilbert_matrices]
    
    print("(b, 1)")

    for i, condition_number in enumerate(condition_numbers, start=1):
        print(f"O número de condicionamento de H{i} é {condition_number}")

    print()
    print("(b, 2)")

    n = 5
    solution = gaussian_elimination(
        get_hilbert_matrix(n), 
        [sum([1/(i + j - 1) for j in range(1, n + 1)]) for i in range(1, n + 1)]
    )

    print(f"A solução do sistema H{n}x = b{n} é x = {solution}")


if __name__ == '__main__':
    main()
