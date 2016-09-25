# https://codility.com/programmers/lessons/7-stacks_and_queues/fish/
# TC: O(N)
# SC: O(1)
# python 2.7.13

def solution(A, B):
    N = len(A)
    stack = []
    for i in range(0, N):
        if len(stack) == 0 or B[i] == 1:
            stack.append(i)
        elif B[i] == 0:
            be_eaten = False
            while len(stack) != 0 and B[stack[-1]] == 1:
                index = stack[-1]
                if A[index] < A[i]:
                    stack.pop()
                    continue
                else:
                    be_eaten = True
                    break;
            if not be_eaten:
                stack.append(i)
    return len(stack)

if __name__ == '__main__':
    assert solution([4,3,2,1,5], [0,1,0,0,0]) == 2
