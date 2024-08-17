from collections import Counter

# Function definition
def majorityElement(nums):
# counter which counts
    counts = Counter(nums)
    print(counts)
    return max(counts.keys(), key = counts.get)











# driver code
nums = [2, 2, 1, 1, 1, 2, 2]

# Result
result = majorityElement(nums)
print("The majority element in the nums array is", result)