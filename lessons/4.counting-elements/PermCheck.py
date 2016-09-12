# https://codility.com/programmers/lessons/4-counting_elements/perm_check/
# TC: O(N)
# SC: O(1)
# python 2.7.13

def solution(A):
    N = len(A)
    temp = 0
    for i in range(0, N):
        temp ^= i+1
        temp ^= A[i]
    if temp != 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    assert solution([4,1,3,2]) == 1
    assert solution([4,1,3]) == 0

