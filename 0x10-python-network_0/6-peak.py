#!/usr/bin/env python3

"""
Write a function that finds a peak in a list of unsorted integers.
"""

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
        return find_peak(lst[:mid])  # Recursively search left half
    elif peak < lst[mid + 1]:
        return find_peak(lst[mid + 1:])  # Recursively search right half
    else:
        return peak  # Current element is a peak
