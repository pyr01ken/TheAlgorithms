def rotate(s, k):
    dubble_s = s + s
    if k <= len(s):
        return dubble_s[k:k+len(s)]
    else:
        return dubble_s[k-len(s):k]
    
print(rotate('Alek', 2)) # => "ekAl"
