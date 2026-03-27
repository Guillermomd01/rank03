def twist(arr: list[int]) -> list[int]:
    # j is the index used to iterate through the array
    j: int = 0

    # len will store the length of the input array
    len: int = 0

    # ret will store the array after one rotation
    ret: list[int] = []

    # Calculate the length of the array
    for i in arr:
        len += 1

    # Loop through the array to build the rotated array
    while j < len - 1:
        if j == 0:
            # On the first iteration, add the last element first (rotation)
            # then add the first element of the original array
            ret.append(arr[-1])
            ret.append(arr[0])
        else:
            # For all other positions, add the element at index j
            ret.append(arr[j])
        j += 1

    # Return the array after one right rotation
    return ret


def twist_sequence(arr: list[int], k: int) -> list[int]:
    # If k is 0 or the array is empty, return the array unchanged
    if k == 0 or not arr:
        return arr

    # Initialize loop counter
    j: int = 0

    # Start with the original array
    ret: list[int] = arr

    # Apply the single-step rotation k times
    while j < k:
        ret = twist(ret)  # Rotate the array by one step
        j += 1

    # Return the array after k rotations
    return ret

def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr: return []
    k %= len(arr)
    return arr[-k:] + arr[:-k]
def twist_sequence(arr: list[int], k: int) -> list[int]:
    for _ in range(0,k):
        arr = arr.insert(0, arr.pop())
    return arr
# Test cases
print(twist_sequence([1, 2, 3, 4, 5], 0))  # No rotation, returns [1, 2, 3, 4, 5]
print(twist_sequence([1, 2, 3, 4, 5], 1))  # Rotate by 1, returns [5, 1, 2, 3, 4]
print(twist_sequence([1, 2, 3, 4, 5], 2))  # Rotate by 2, returns [4, 5, 1, 2, 3]
print(twist_sequence([1, 2, 3, 4, 5], 7))  # Rotate by 7 (equivalent to 2), returns [4, 5, 1, 2, 3]
print(twist_sequence([], 3))               # Empty array, returns []
