def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged


def merge_sort(lst):
    if len(lst) <= 1:
        return lst  
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])  
    right_half = merge_sort(lst[mid:]) 
    return merge(left_half, right_half)