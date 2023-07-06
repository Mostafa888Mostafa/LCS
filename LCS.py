def find_lcs(dna1, dna2):
    m = len(dna1)
    n = len(dna2)
    lcs = [[0] * (n + 1) for _ in range(m + 1)]