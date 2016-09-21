# https://codesays.com/2014/solution-to-triangle-by-codility/
# TC: O(NlogN)
# SC: O(1)
# python 2.7.13

def solution(A):
    N = len(A)
    if N < 3:
        return 0
    # O(nlogn) sorting
    A.sort()
    for i in range(0, N-2):
        # After sorting, we have A[i] <= A[i+1] <= A[i+2]
        # therefore, A[i] < A[i+1] + A[i+2] hold,
        # and A[i+1] < A[i] + A[i+2] hold.
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0

if __name__ == '__main__':
    assert solution([10,2,5,1,8,20]) == 1
