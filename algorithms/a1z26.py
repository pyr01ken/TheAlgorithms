def encode(val: str) -> list:
    return [ord(i) for i in val]


def decode(val: list) -> str:
    return "".join((chr(i) for i in val))


print(encode('mohammad')) # => [109, 111, 104, 97, 109, 109, 97, 100]
print(decode([109, 111, 104, 97, 109, 109, 97, 100])) # => 'mohammad'
