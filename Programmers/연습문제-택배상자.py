### level 2 ###

# 1차: 221223

'''
연습문제 - 택배상자 (131704)
'''


from collections import deque

def solution(order):
    order = deque(order)
    boxes = deque(range(1, len(order) + 1))
    container, sub_container = [], []

    while boxes:
        sub_container.append(boxes.popleft())

        while sub_container[-1] == order[0]:
            container.append(sub_container.pop())
            order.popleft()

            if not sub_container:
                break

    return len(container)

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))