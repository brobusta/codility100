# https://codility.com/programmers/lessons/8-leader/dominator/
# TC: O(N)
# SC: O(1)
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
    # check if candidate is a dominator
    count = 0
    index = -1
    for i in range(0, N):
        if candidate == A[i]:
            count += 1
            index = i
    dominator = -1
    if count > N / 2:
        dominator = index
    return dominator

if __name__ == '__main__':
    assert solution([3,4,3,2,3,-1,3,3]) == 7
