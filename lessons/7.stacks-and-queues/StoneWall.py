# https://codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
# TC: O(N)
# SC: O(1)
# python 2.7.13

def solution(H):
    N = len(H)
    stack = []
    num_block = 0
    for i in range(0, N):
        stop = False
        while len(stack) != 0 and not stop:
            top = stack[-1]
            if top > H[i]:
                stack.pop()
                continue
            elif top == H[i]:
                stop = True
            else:
               stack.append(H[i])
               num_block += 1
               stop = True
        if not stop:
            stack.append(H[i])
            num_block += 1
    return num_block

if __name__ == '__main__':
    assert solution([8,8,5,7,9,8,7,4,8]) == 7
