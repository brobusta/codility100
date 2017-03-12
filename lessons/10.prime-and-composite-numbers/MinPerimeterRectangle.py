# https://codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/
# TC: O(logN)
# SC: O(1)
# python 2.7.13

def solution(N):
    from math import sqrt
    a = int(sqrt(N))
    while a > 0:
        if N % a == 0:
            return 2 * (a + (N / a))
        a -= 1
    return 0

if __name__ == '__main__':
    assert solution(30) == 22
