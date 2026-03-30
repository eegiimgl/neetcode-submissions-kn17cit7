class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(0, len(position)):
            cars.append((position[i], speed[i]))
        
        cars_sorted = sorted(cars, key=lambda x: x[0], reverse=True)

        stack = []
        for car in cars_sorted:
            time = (target - car[0]) / car[1]
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)

        return len(stack)



"""
        0   1   2   3   4   5   6   7   8   9   10
car 1                                           c1
                                                c2
                        c3
                                                c4


position = [4,1,0,7]
speed = [2,2,1,1]

    (0;1) (1;2) (4;2) (7;1)
      10   4.5    3     3


      [3, 4.5, 10]
"""