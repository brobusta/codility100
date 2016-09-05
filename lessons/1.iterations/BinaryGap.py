# https://codility.com/programmers/lessons/1-iterations/binary_gap/
# python 2.7.13
def solution(N):
    maxGap = 0
    currentGap = 0
    # skip zeros at tail, assume that N > 0
    while (N & 0x1) == 0:
        N = N >> 1
    # calculate the gap
    while N != 0:
        lsb = N & 0x1
        if lsb == 0x1:
            maxGap = max(maxGap, currentGap)
            currentGap = 0
        else:
            currentGap += 1
        N = N >> 1
    return maxGap

if __name__ == '__main__':
    assert solution(9) == 2
    assert solution(529) == 4
    assert solution(20) == 1
    assert solution(15) == 0

