# https://codility.com/programmers/lessons/4-counting_elements/frog_river_one/
# TC:
# SC:
# python 2.7.13

def solution(X, A):
    N = len(A)
    fell = [False] * (X+1)
    remain = X
    for i in range(0, N):
        if 0 < A[i] <= X and not fell[A[i]]:
            fell[A[i]] = True
            remain -= 1
            if remain == 0:
                return i
    return -1

if __name__ == '__main__':
    assert solution(5, [1,3,1,4,2,3,5,4]) == 6
