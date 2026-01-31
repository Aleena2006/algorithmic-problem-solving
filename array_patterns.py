# Two-pointer technique: Remove duplicates from sorted array
def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k

# Maximum subarray sum (Kadane’s Algorithm)
def max_subarray(nums):
    curr = max_sum = nums[0]
    for n in nums[1:]:
        curr = max(n, curr + n)
        max_sum = max(max_sum, curr)
    return max_sum

print(remove_duplicates([1,1,2,2,3]))
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
