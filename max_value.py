# def max_value(nums):
#     return max(nums)


def max_value(nums):
    largest = nums[0]
    for num in nums[1:]:
        if num>largest:
            largest = num
    return largest