# https://codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/
# TC: O(N)
# SC: O(1)
# python 2.7.13

def solution(A):
    N = len(A) # N >= 1
    max_ending_here = max_total = A[0]
    for i in range(1,N):
        max_ending_here = max(A[i], max_ending_here + A[i])
        max_total = max(max_ending_here, max_total)
    return max_total

if __name__ == '__main__':
    assert solution([3,2,-6,4,0]) == 5
