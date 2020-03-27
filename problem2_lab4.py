def split(s):
    half, rem = divmod(len(s), 2)
    if rem:
        half += 1
    return s[:half], s[half:]
def front_back(a, b):
    front_a ,back_a = split(a)
    front_b ,back_b = split(b)
    return (front_a + front_b  ),(back_a + back_b)
z=front_back("abcde","abcd")
print(z)