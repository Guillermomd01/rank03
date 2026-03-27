def echo_validator(text: str) -> bool:
    s = "".join(filter(str.isalnum, text.lower()))
    return s == s[::-1]


# Test cases to verify the function
print(echo_validator("radar"))                        # True
print(echo_validator("Level"))                        # True
print(echo_validator("A man a plan a canal Panama"))  # True
print(echo_validator("Hello world"))                  # False
print(echo_validator(""))                             # True
