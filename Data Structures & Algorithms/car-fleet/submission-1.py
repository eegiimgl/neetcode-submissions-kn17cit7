class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []
        for car in cars:
            time = (target - car[0]) / car[1]
            if len(stack) == 0:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        return len(stack)