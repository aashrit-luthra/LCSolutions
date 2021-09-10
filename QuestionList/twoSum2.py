class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i < j:
            sumOfPair = numbers[i] + numbers[j]
            if sumOfPair == target:
                return [i+1,j+1]
            elif sumOfPair < target:
                i += 1
            else:
                j -= 1
        return [-1,-1]