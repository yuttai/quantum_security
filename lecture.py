def exp_mod(b, d, n):
    d_binary = bin(d)
    d_binary_without_0b = d_binary[2:]
    b_j = b
    b_d = 1
    for d_j in reversed(d_binary_without_0b):
        if d_j == '1':
            b_d = (b_d * b_j) % n
        b_j = (b_j ** 2) % n
    return b_d


print(exp_mod(10, 5, 91))
print(exp_mod(82, 29, 91))


def exp_mod_while(b, d, n):
    b_j = b
    b_d = 1
    while d:
        if d % 2:
            b_d = (b_d * b_j) % n
        b_j = (b_j ** 2) % n
        d //= 2
    return b_d


print(exp_mod_while(10, 5, 91))
print(exp_mod_while(82, 29, 91))
