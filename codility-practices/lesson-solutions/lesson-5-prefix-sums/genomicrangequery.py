def solution_2(S, P, Q):  # this solution gives 100% correctness but 62 overall
    impact = {"A": 1, "C": 2, "G": 3, "T": 4}
    output = []

    for i in range(len(P)):
        e = [impact[n] for n in S[P[i]:Q[i] + 1]]
        output.append(min(e))

    return output


def solution(S, P, Q):
    output = []
    for i in range(len(P)):
        if 'A' in S[P[i]:Q[i] + 1]:
            output.append(1)
        elif 'C' in S[P[i]:Q[i] + 1]:
            output.append(2)
        elif 'G' in S[P[i]:Q[i] + 1]:
            output.append(3)
        elif 'T' in S[P[i]:Q[i] + 1]:
            output.append(4)
    return output


if __name__ == "__main__":
    _s = "CAGCCTA"
    _p = [2, 5, 0]
    _q = [4, 5, 6]
    print(solution(_s, _p, _q))
