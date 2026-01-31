# Frequency counting using hashing
def most_frequent(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    return max(freq, key=freq.get)

# Two Sum using hashing
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

print(most_frequent([1, 3, 2, 1, 4, 1]))
print(two_sum([2, 7, 11, 15], 9))
