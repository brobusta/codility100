# https://codility.com/programmers/lessons/5-prefix_sums/passing_cars/
# TC: O(N)
# SC: O(1)
# python 2.7.13

def solution(A):
    N = len(A)
    numZeroes = 0
    total = 0
    for i in range(0, N):
        if A[i] == 0:
            numZeroes += 1
        elif A[i] == 1:
            total += numZeroes
            if total > 1000000000:
                return -1
    return total

if __name__ == '__main__':
    assert solution([0, 1, 0, 1, 1]) == 5
