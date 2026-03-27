
def pattern_tracker(text: str) -> int:
    prev_was_digit = False
    count = 0
    for c in text:
        if c.isdigit():
            if prev_was_digit:
                count += 1
            prev_was_digit = True
        else:
            prev_was_digit = False
    return count
