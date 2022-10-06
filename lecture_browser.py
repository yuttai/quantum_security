def get_quotient_remainder_list(a, b):
    u"""Assume a >= b"""
    quotient_remainder_list = [divmod(a, b)]
    while quotient_remainder_list[-1][1] != 0:
        quotient_remainder_list.append(divmod(
            quotient_remainder_list[-2][1] if len(quotient_remainder_list) > 1 else b,
            quotient_remainder_list[-1][1]))
    return quotient_remainder_list


def gcd_while(a, b):
    if a < b:
        return gcd_while(b, a)
    remainders = [a % b]
    while remainders[-1] != 0:
        remainders.append(
            (remainders[-2] if len(remainders) > 1 else b) % remainders[-1])
    return \
        remainders[-2] if len(remainders) > 1 else \
        b


print(gcd_while(72, 5))
print(gcd_while(5, 72))
