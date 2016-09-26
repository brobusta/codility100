# https://codility.com/programmers/lessons/7-stacks_and_queues/nesting/
# TC: O(N)
# SC: O(1)
# python 2.7.13

def solution(S):
    N = len(S)
    if N == 0:
        return 1
    if N % 2 != 0:
        return 0
    stack = []
    for i in range(0, N):
        if S[i] == '(':
            stack.append(S[i])
        elif S[i] == ')':
            if len(stack) == 0:
                return 0
            else:
                top = stack.pop()
                if top != '(':
                    return 0
    if len(stack) == 0:
        return 1
    return 0

if __name__ == '__main__':
    assert solution("(()(())())") == 1
    assert solution("())") == 0
    assert solution(")(") == 0
