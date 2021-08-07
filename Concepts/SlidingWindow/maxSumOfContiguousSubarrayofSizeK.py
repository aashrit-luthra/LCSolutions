def maxSum(arr, k):
    if len(arr) < k:
        return -1
    
    idx = 0
    globalMax = float('-inf')
    runningSum = 0
    for idx in range(len(arr)):
        runningSum += arr[idx]
        if idx >= k - 1:
            globalMax = max(globalMax, runningSum)
            runningSum -= arr[idx - k + 1]
    return globalMax

print(maxSum([4,2,1,7,8,1,2,8,1,0], 3))

