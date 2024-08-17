# fun def
def sortColors(nums):
    p0 = curr = 0
    p2 = len(nums)-1

    # using while loop
    while curr <= p2:
        if nums[curr] == 0:
            # Swap nums of curr and nums of p0
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            # swap nums of curr and nums of p2
            nums[p2], nums[curr] = nums[curr], nums[p2]
            p2 -= 1
        else:
            curr += 1
    return nums







# Driver code
nums = [2, 0, 2, 1, 1, 0]
result = sortColors(nums)
print("The sorted colors are ", result)