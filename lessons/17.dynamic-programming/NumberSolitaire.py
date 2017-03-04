# https://codility.com/programmers/lessons/17-dynamic_programming/
# TC: O(N)
# SC: O(N)
# python 2.7.13

def solution(A):
    N = len(A)
    max_here = [0] * N
    max_here[0] = A[0]
    for i in range(1, N):
        if i <= 6:
            max_here[i] = A[i] + max(max_here[0:i])
        else:
            max_here[i] = A[i] + max(max_here[i-6:i])
    return max_here[N-1]

if __name__ == '__main__':
    assert solution([0, -4, -5, -2, -7, -9, -3, -10]) == -12
