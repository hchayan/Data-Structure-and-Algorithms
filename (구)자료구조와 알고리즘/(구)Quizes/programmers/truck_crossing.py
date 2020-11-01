

def solution(bridge_length, weight, truck_weights):
    time = []
    on_bridge = []

    ans = 0

    while len(truck_weights) > 0 or len(on_bridge) > 0:

        if len(time) !=0 and time[0] == bridge_length:
            time.pop(0)
            on_bridge.pop(0)

        if len(truck_weights) != 0 and sum(on_bridge)+truck_weights[0] <= weight:
            on_bridge.append(truck_weights.pop(0))
            time.append(0)

        time = [i+1 for i in time]
        ans+=1
    return ans
