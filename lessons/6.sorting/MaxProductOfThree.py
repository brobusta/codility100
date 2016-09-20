# https://codility.com/programmers/lessons/6-sorting/max_product_of_three/
# TC:
# SC:
# python 2.7.13

def solution(A):
    N = len(A)
    # O(nlogn) sorting
    A.sort()
    ret = max(A[0]*A[1]*A[-1], A[-3]*A[-1]*A[-2])
    return ret

if __name__ == '__main__':
    assert solution([-3,1,2,-2,5,6]) == 60
