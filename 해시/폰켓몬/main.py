def solution(nums):
    can_select_nums = len(nums) // 2
    distinct_nums = len(set(nums))
    return min(can_select_nums, distinct_nums)
