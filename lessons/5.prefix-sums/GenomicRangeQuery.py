# https://codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
# TC: O(N+M)
# SC: O(N+M)
# python 2.7.13

def solution(S, P, Q):
    N = len(S)
    M = len(P)
    # calculate prefix sum
    psA = [0] * (N+1)
    psC = [0] * (N+1)
    psG = [0] * (N+1)
    psT = [0] * (N+1)
    numA = 0
    numC = 0
    numG = 0
    numT = 0
    for i in range(1, N+1):
        nuc = S[i-1]
        if nuc == 'A':
            numA += 1
        elif nuc == 'C':
            numC += 1
        elif nuc == 'G':
            numG += 1
        elif nuc == 'T':
            numT += 1
        psA[i] = numA
        psC[i] = numC
        psG[i] = numG
        psT[i] = numT
    ret = [0] * M
    for i in range(0, M):
        countA = count_total(psA, P[i], Q[i])
        if countA > 0:
            ret[i] = 1
            continue
        countC = count_total(psC, P[i], Q[i])
        if countC > 0:
            ret[i] = 2
            continue
        countG = count_total(psG, P[i], Q[i])
        if countG > 0:
            ret[i] = 3
            continue
        countT = count_total(psT, P[i], Q[i])
        if countT > 0:
            ret[i] = 4
            continue
    return ret

def count_total(pS, x, y):
    return pS[y+1] - pS[x]

if __name__ == '__main__':
    assert solution("CAGCCTA",[2,5,0],[4,5,6]) == [2,4,1]
