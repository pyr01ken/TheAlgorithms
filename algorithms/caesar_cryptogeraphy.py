from string import ascii_letters

def encrypt(string, key):
    alpha = ascii_letters
    result = ''

    for char in string:
        if char not in alpha:
            result += char
        else:
            new_key = (alpha.index(char) + key) % len(alpha)
            result += alpha[new_key]
    
    return result

def decrypt(string, key):
    key *= -1
    return encrypt(string, key)

def brute_force(string):
    alpha = ascii_letters
    key = 0
    result = ''
    brute_force_data = {} 

    while key <= len(alpha):
        result = decrypt(string, key)
        brute_force_data[key] = result
        result = ''
        key += 1
    
    return brute_force_data

# print(encrypt('mohammad', 1)) # => 'npibnnbe'
# print(decrypt('npibnnbe', 1)) # => 'mohammad'

print(brute_force('npibnnbe'))