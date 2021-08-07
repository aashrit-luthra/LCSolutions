def smallestSubarrayWithSumGreaterThanK(arr, k):
    j = 0
    runningSum = 0
    minSubarraySize = float('inf')
    for i in range(len(arr)):
        runningSum += arr[i]
        while runningSum >= k:
            minSubarraySize = min(minSubarraySize, i - j + 1)
            runningSum -= arr[j]
            j += 1
    return minSubarraySize

print(smallestSubarrayWithSumGreaterThanK([4,2,2,7,8,1,2,8,10],8))