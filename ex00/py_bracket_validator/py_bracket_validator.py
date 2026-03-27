def brackets(text: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in text:
        if char in '([{':
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

print(brackets("()"))         # True
print(brackets("({[abc]})"))       # True
print(brackets("([)]"))      # False
print(brackets("("))            # False
print(brackets("abc{[()]}"))    # True
print(brackets(""))              # True