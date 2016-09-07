# https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# python 2.7.13

def solution(A, K):
    N = len(A)
    if (N==0) or (K==0):
        return A
    if K > N:
        K = K % N
    return A[-K:] + A[:-K]

if __name__ == '__main__':
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
