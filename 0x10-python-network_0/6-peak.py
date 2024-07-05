# Write a function that finds a peak in a list of unsorted integers.
def find_peak(lst):
    size = len(lst)
    if size == 0:
        return None
    elif size == 1:
        return lst[0]
    elif size == 2:
        return max(lst)

    mid = size // 2
    peak = lst[mid]

    if peak < lst[mid - 1]:
        return find_peak(lst[:mid])
    elif peak < lst[mid + 1]:
        return find_peak(lst[mid + 1:])
    else:
        return peak
