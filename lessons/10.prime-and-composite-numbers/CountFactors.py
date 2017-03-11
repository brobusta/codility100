# https://codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/
# TC: O(sqrt(N))
# SC: O(1)
# python 2.7.13

def solution(N):
    num_factor = 0
    i = 1
    while (i * i < N):
        if N % i == 0:
            num_factor += 2
        i += 1
    if (i * i == N):
        num_factor += 1
    return num_factor

if __name__ == '__main__':
    assert solution(24) == 8
