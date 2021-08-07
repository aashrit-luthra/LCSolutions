def kadaneAlgorithm(arr):
    currentSum = 0
    maxSum = float('-inf')
    for i in range(len(nums)):
        currentSum = max(nums[i], currentSum + nums[i])
        maxSum = max(maxSum, currentSum)
    return maxSum