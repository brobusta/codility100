# https://codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/
# TC: O(N)
# SC: O(1)
# python 2.7.13

def solution(A):
    N = len(A)
    if N == 0:
        return 0
    max_profit_here = 0
    max_profit_total = 0
    for i in range(1, N):
        max_profit_here = max(0, max_profit_here + A[i] - A[i-1])
        max_profit_total = max(max_profit_here, max_profit_total)
    return max_profit_total

if __name__ == '__main__':
    assert solution([23171, 21011, 21123, 21366, 21013, 21367]) == 356
