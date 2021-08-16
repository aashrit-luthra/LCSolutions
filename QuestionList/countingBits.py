import math
def convertIntToBinary(n):
    counter = 0
    while n:
        exponent = floor(math.log(n, 2))
        n -= 2**exponent
        counter += 1
    return counter

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0 for i in range(n+1)]
        for i in range(n+1):
            output[i] = convertIntToBinary(i)
        return output