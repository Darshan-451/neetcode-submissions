class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  #It combines the position and speed of each car.
        stack = [] #This stack stores the arrival times of different car fleets.
        for position, speed in cars: #We visit every car one by one.
            time = (target - position) / speed
            if not stack or time > stack[-1]: #not stack: Is the stack empty? If yes, this car creates a new fleet.
                stack.append(time)
        return len(stack)