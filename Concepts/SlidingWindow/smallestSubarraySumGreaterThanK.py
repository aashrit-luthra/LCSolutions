def smallestSubarraySumGreaterThanK(arr, k):
    currentSum = 0
    minSum = float('inf')
    left = 0
    for i in range(len(arr)):
        currentSum += arr[i]
        while currentSum >= k:
            minSum = min(minSum, currentSum)
            currentSum -= arr[left]
            left += 1
    return minSum

print(smallestSubarrayWithSumGreaterThanK([4,2,2,7,8,1,2,8,1,0], 8))
        
            

