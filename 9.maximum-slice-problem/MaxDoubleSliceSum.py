# https://codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/
# TC: O(N)
# SC: O(N)
# python 2.7.13

def solution(A):
    N = len(A) #N>=3
    max_ending_here = [0] * N
    max_beginning_here = [0] * N
    for i in range(1, N-2):
        max_ending_here[i] = max(0, max_ending_here[i-1] + A[i])
    for i in range(N-2,1,-1):
        max_beginning_here[i] = max(0, A[i] + max_beginning_here[i+1])
    max_total = 0
    for i in range(1,N-1):
        max_total = max(max_total, max_ending_here[i-1] + max_beginning_here[i+1])
    return max_total

if __name__ == '__main__':
    assert solution([3,2,6,-1,4,5,-1,2]) == 17
