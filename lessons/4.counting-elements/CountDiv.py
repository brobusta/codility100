# https://codility.com/programmers/lessons/5-prefix_sums/count_div/
# TC: O(1)
# SC: O(1)
# python 2.7.13

def solution(A, B, K):
    ret = B/K - A/K
    if A % K == 0:
        ret += 1
    return ret

if __name__ == '__main__':
    assert solution(6, 11, 2) == 3
