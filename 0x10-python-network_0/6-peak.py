def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    def find_peak_util(nums, low, high):
        mid = (low + high) // 2
        if (mid == 0 or nums[mid - 1] <= nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] <= nums[mid]):
            return nums[mid]
        elif mid > 0 and nums[mid - 1] > nums[mid]:
            return find_peak_util(nums, low, mid - 1)
        else:
            return find_peak_util(nums, mid + 1, high)

    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1)
