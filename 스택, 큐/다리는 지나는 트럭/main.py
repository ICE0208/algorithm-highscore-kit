from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_deq = deque(truck_weights)
    on_bridge = deque()

    sec = 0
    remain_weight = weight
    while truck_deq or on_bridge:
        sec += 1
        if on_bridge and (on_bridge[0][0] <= sec - bridge_length):
            poped = on_bridge.popleft()
            remain_weight += poped[1]

        if truck_deq and (truck_deq[0] <= remain_weight):
            poped = truck_deq.popleft()
            on_bridge.append((sec, poped))
            remain_weight -= poped

    return sec
