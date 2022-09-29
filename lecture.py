def char2utf8(input_character):
    input_unicode = ord(input_character)
    input_binary = bin(input_unicode)
    input_binary_without_0b = input_binary[2:]
    if len(input_binary_without_0b) <= 7:
        return hex(input_unicode)
    else:
        z = input_binary_without_0b[-6:]
        if len(input_binary_without_0b) <= 11:
            pass
        else:
            y = input_binary_without_0b[-12:-6]
            return hex(int(
                '0b1110{:0>4}10{}10{}'.format(
                    input_binary_without_0b[-16:-12],
                    y,
                    z) if len(input_binary_without_0b) <= 16 else None,
                2))


print(char2utf8('台'))
print(char2utf8('台') == '0xe58fb0')
print(char2utf8(' '))
print(char2utf8(' ') == '0x20')


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


def gcd_while(a, b):
    if a < b:
        return gcd_while(b, a)
    quotient_remainder_list = [divmod(a, b)]
    while quotient_remainder_list[-1][1] != 0:
        quotient_remainder_list.append(divmod(
            quotient_remainder_list[-2][1] if len(quotient_remainder_list) > 1 else b,
            quotient_remainder_list[-1][1]))
    return \
        quotient_remainder_list[-2][1] if len(quotient_remainder_list) > 1 else \
        b


print(gcd_while(72, 5))
print(gcd_while(5, 72))

