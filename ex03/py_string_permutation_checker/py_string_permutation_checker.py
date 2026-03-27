def string_permutation_checker(s1: str, s2: str) -> bool:
    # First compare the lengths
    if len(s1) != len(s2):
        return False
    # Save all the char of s1 in a list
    chars = []
    for c in s1:
        chars.append(c)

    for c in s2:
        # Check if the char is not in the avabible chars
        if c not in chars:
            return False
        else:
            # We have to remove it cause if we have a string like a Test, and
            # test its gonna return true
            chars.remove(c)
    return True

def string_permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)