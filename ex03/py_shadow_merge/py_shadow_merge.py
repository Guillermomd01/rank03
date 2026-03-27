def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    # ret will store all elements from both input lists
    ret: list[int] = []

    # len represents the total number of elements in ret
    len: int = 0

    # j is used as an index for sorting
    j: int = 0

    # tmp is a temporary variable used for swapping values
    tmp: int = 0

    # First loop: copy all elements from list1 into ret
    for i in list1:
        ret.append(i)
        len += 1

    # Second loop: copy all elements from list2 into ret
    for i in list2:
        ret.append(i)
        len += 1

    # Sorting loop (bubble sort logic)
    # We compare each element with the next one and swap them if needed
    while j < len - 1:
        if ret[j] > ret[j + 1]:
            # Swap the two elements
            tmp = ret[j]
            ret[j] = ret[j + 1]
            ret[j + 1] = tmp

            # Restart from the beginning after a swap
            j = 0
            continue
        else:
            # Move to the next index if elements are already in order
            j += 1

    # Return the merged and sorted list
    return ret

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    return sorted(list1 + list2)
# Test cases
print(shadow_merge([1, 3, 5], [2, 4, 6]))   # [1, 2, 3, 4, 5, 6]
print(shadow_merge([1, 2, 2], [2, 3]))      # [1, 2, 2, 2, 3]
print(shadow_merge([], [1, 2, 3]))          # [1, 2, 3]
print(shadow_merge([4, 5, 6], []))          # [4, 5, 6]
print(shadow_merge([], []))                 # []
