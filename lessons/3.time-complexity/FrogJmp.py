# https://codility.com/programmers/lessons/3-time_complexity/frog_jmp/
# TC: O(1)
# SC: O(1)
# python 2.7.13

def solution(X, Y, D):
    distance = Y - X
    if distance % D == 0:
        return distance / D
    else:
        return (distance / D) + 1

if __name__ == '__main__':
    assert solution(10, 85, 30) == 3
