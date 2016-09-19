# https://codility.com/programmers/lessons/6-sorting/distinct/
# TC: O(NlogN)
# SC: O(1)
# python 2.7.13

def solution(A):
    N = len(A)
    if N == 0:
        return 0
    # O(nlogn) sorting built-in
    A.sort()
    distinct = 1
    for k in range(1, N):
        if A[k] != A[k-1]:
            distinct += 1
    return distinct

if __name__ == '__main__':
    assert solution([2,1,1,2,3,1]) == 3

