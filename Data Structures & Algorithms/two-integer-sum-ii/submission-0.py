class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap= {}
        for i, num in enumerate(numbers):
            current= target - num
            if current in hashmap:
                return [hashmap[current]+1, i+1]
            hashmap[num]=i


