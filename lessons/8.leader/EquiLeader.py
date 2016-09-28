# https://codility.com/programmers/lessons/8-leader/equi_leader/
# TC: O(N)
# SC: O(N)
# python 2.7.13

def solution(A):
    N = len(A)
    if N == 0:
        return -1
    # A stack
    size = 0
    top = -1
    for i in range(0, N):
        if size == 0:
            top = A[i]
            size += 1
        else:
            if top != A[i]:
                # remove top from stack
                size -= 1
            else:
                size += 1
    candidate = -1
    if size > 0:
        candidate = top
    # check if candidate is a leader
    count = 0
    leader_so_far = [0] * N
    for i in range(0, N):
        if candidate == A[i]:
            count += 1
        leader_so_far[i] = count
    if count <= N / 2:
        # no leader found
        return 0
    # find equi-leader
    ret = 0
    for i in range(0, N):
        if leader_so_far[i] > (i+1)/2 and (count - leader_so_far[i]) > (N-i-1)/2:
            ret += 1
    return ret

if __name__ == '__main__':
    assert solution([4,3,4,4,4,2]) == 2
