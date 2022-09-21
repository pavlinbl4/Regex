import re


def increment_string(s):
    digit = re.findall(r'\d+$', s)
    digit_len = len(digit)
    if digit_len == 0:
        new_digit = '1'
        s = s + '0'
    else:
        new_digit = str(int(digit[0]) + 1)
        if len(digit[0]) > len(new_digit):
            new_digit = '0' * (len(digit[0]) - len(new_digit)) + new_digit
    return re.sub(r'\d+$', new_digit, s)


print(increment_string('foobar0007'))
