# https://codility.com/programmers/lessons/4-counting_elements/max_counters/
# TC: O(max(N,M))
# SC: O(N)
# python 2.7.13

def solution(N, A):
    M = len(A)
    ret = [0]*N
    currMax = 0
    lastMax = currMax
    maxCounterPendingOps = False

    for i in range(0, M):
        if A[i] == N+1:
            maxCounterPendingOps = True
            lastMax = currMax
        elif 1 <= A[i] <= N:
            if maxCounterPendingOps and ret[A[i]-1] < lastMax:
                ret[A[i]-1] = lastMax + 1
            else:
                ret[A[i]-1] += 1
            currMax = max(currMax, ret[A[i]-1])
    if maxCounterPendingOps:
        for i in range(0, N):
            if ret[i] < lastMax:
                ret[i] = lastMax
    return ret

if __name__ == '__main__':
    assert solution(5, [3,4,4,6,1,4,4]) == [3,2,2,4,2]


