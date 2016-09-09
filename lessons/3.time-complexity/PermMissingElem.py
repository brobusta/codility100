# https://codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# TC: O(N)
# SC: O(1)
# python 2.7.13

def solution(A):
    N = len(A)
    missing = N + 1
    for i in range(0, N):
        missing ^= i + 1
        missing ^= A[i]
    return missing

if __name__ == '__main__':
    assert solution([2, 3, 1, 5]) == 4
