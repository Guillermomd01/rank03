def py_string_sculptor(text: str) -> str:
    index = 0
    res = ''
    for c in text:
        if c.isalpha():
            # Check if the index is even or odd
            if index % 2 == 0:
                res += c.lower()
            else:
                res += c.upper()
        else:
            # Add the non alpha char to the res
            res += c
        index += 1
    return res
