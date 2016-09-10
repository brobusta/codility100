# https://codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# TC: O(N)
# SC: O(N)
# python 2.7.13

def solution(A):
    N = len(A)
    total = sum(A)
    leftSum = A[0]
    minimal = abs(total - 2 * leftSum)
    for i in range(1, N - 1):
        leftSum += A[i]
        minimal = min(minimal, abs(total - 2 * leftSum))
    return minimal

if __name__ == '__main__':
    assert solution([3, 1, 2, 4, 3]) == 1
