# https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
# python 2.7.13
# TimeComplexity: O(N)
# SpaceComplexity: O(1)

def solution(A):
    N = len(A)
    unpaired = 0
    for i in range(0, N):
        unpaired ^= A[i]
    return unpaired

if __name__ == '__main__':
    assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
