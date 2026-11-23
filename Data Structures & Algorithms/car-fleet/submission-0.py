class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        c = sorted(list(zip(position, speed)), key=lambda x: x[0], reverse=True)
        s = []
        for i in range(len(c)):
            item = c[i]
            time = (target - item[0]) / item[1]
            next_car = s[-1] if s else None
            if next_car and next_car >= time:
                # stuck in the fleet of next_car
                continue
            else:
                s.append(time)
        return len(s)