# https://codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
# TC: O(N)
# SC: O(1)
# python 2.7.13

# (1) There must be 2-length slice or 3-length slice hold Global Minimum Average (GMA)
# (2) All longer slices can be devided to 2-length slices and/or 3-length slices.

def solution(A):
    N = len(A)
    min_so_far = (A[0] + A[1]) / 2.0
    min_pos = 0
    for i in range(0, N-2):
        # check 2-length slice
        temp2 = (A[i] + A[i+1]) / 2.0
        if temp2 < min_so_far:
            min_so_far = temp2
            min_pos = i
        # check 3-length slice
        temp3 = (A[i] + A[i+1] + A[i+2]) / 3.0
        if temp3 < min_so_far:
            min_so_far = temp3
            min_pos = i
    # check 2 last elements
    temp2last = (A[-1] + A[-2]) / 2.0
    if temp2last < min_so_far:
        min_so_far = temp2last
        min_pos = N - 2
    return min_pos

if __name__ == '__main__':
    assert solution([4,2,2,5,1,5,8]) == 1
