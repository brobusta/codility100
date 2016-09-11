# https://codility.com/programmers/lessons/4-counting_elements/missing_integer/
# TC: O(N)
# SC: O(N)
# python 2.7.13

def solution(A):
    N = len(A)
    occur = [False] * (N+1)
    for i in range(0, N):
        if (A[i] > 0) and (A[i] < N+1) and not occur[A[i]]:
            occur[A[i]] = True
    for i in range(1, N+1):
        if not occur[i]:
            return i
    return N+1

if __name__ == '__main__':
    assert solution([1,2,3,4,5]) == 6
    assert solution([1,3,6,4,1,2]) == 5
