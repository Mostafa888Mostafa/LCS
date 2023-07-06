def find_lcs(dna1, dna2):
    m = len(dna1)
    n = len(dna2)
    lcs = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i - 1] == dna2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    result = ""
    i, j = m, n
    while i > 0 and j > 0:
        if dna1[i - 1] == dna2[j - 1]:
            result = dna1[i - 1] + result
            i -= 1
            j -= 1
        elif lcs[i - 1][j] > lcs[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    return lcs[m][n], result

def print_lcs(dna1, dna2):
    m = len(dna1)
    n = len(dna2)
    lcs = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i - 1] == dna2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    result = ""
    i, j = m, n
    while i > 0 and j > 0:
        if dna1[i - 1] == dna2[j - 1]:
            result = dna1[i - 1] + result
            i -= 1
            j -= 1
        elif lcs[i - 1][j] > lcs[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return result

