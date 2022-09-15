def char2utf8(input_character):
    input_unicode = ord(input_character)
    input_binary = bin(input_unicode)
    input_binary_without_0b = input_binary[2:]
    z = input_binary_without_0b[-6:]
    y = input_binary_without_0b[-12:-6]
    x = input_binary_without_0b[-16:-12]
    input_utf8 = '0b1110{:0>4}10{}10{}'.format(x, y, z)
    return hex(int(input_utf8, 2))


print(char2utf8('台'))
print(char2utf8('台') == '0xe58fb0')
