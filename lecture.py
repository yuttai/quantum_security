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
