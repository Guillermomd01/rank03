def whisper_cipher(text: str, shift) -> str:
    result = ''
    for c in text:
        # If it alphabetical
        if c.isalpha():
            # We have to get the ascii lower or upper A so we can use it
            base = ord('a') if c.islower() else ord('A')
            # Chr means go back to character, ord means give me the
            # ascii code of a char
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result
