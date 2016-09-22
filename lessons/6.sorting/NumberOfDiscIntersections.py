# https://codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
# TC: O(NlogN)
# SC: O(N)
# python 2.7.13

def solution(A):
    N = len(A)
    if N == 0 or N == 1:
        return 0
    lefts = [0] * N
    rights = [0] * N
    for i in range(0, N):
        lefts[i] = i - A[i]
        rights[i] = i + A[i]
    lefts.sort()
    rights.sort()
    left_active = 0
    left_count = 0
    intersects = 0
    for i in range(0, N):
        curr_right = rights[i]
        # remove one which corresponds to curr_right
        left_active -= 1
        while (left_count < N and lefts[left_count] <= curr_right):
            left_count += 1
            left_active += 1
        intersects += left_active
        if intersects > 10000000:
            return -1
    return intersects

if __name__ == '__main__':
    assert solution([1,5,2,1,4,0]) == 11
