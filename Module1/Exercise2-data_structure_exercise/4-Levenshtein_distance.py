def levenshtein_distance(source, target):
    M = len(source) + 1
    N = len(target) + 1
    D = [[None for _ in range(N)] for _ in range(M)]

    for i in range(M):
        D[i][0] = i
    for i in range(N):
        D[0][i] = i

    for i in range(1, M):
        for j in range(1, N):
            if source[i - 1] == target[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] +
                              1, D[i - 1][j - 1] + 1)

    return D[M - 1][N - 1]

if __name__ == "__main__":
    source = "you"
    target = "yu"
    print(levenshtein_distance(source, target))

    source = "kitten"
    target = "sitting"
    print(levenshtein_distance(source, target))
