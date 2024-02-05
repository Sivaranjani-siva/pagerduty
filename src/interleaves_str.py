def interleave_str(str_1, str_2):
    interleaved_str = ''.join([a + b for a, b in zip(str_1, str_2)])
    if len(str_1) > len(str_2):
        interleaved_str += str_1[len(str_2):]
    else:
        interleaved_str += str_2[len(str_1):]
    return interleaved_str

str_1 = "AAAA"
str_2 = "1234567"
interleaved_res = interleave_str(str_1, str_2)
print(interleaved_res)