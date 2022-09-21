import re


def to_integer(text):
    # match = re.findall(r'^[-+]?\d+[^\s]$|^[-+]?0b[01]+[^\s]$|^[-+]?0x[0-9A-Fa-f]+[^\s]$|^[-+]?0o[0-7]+[^\s]$', text)
    match = re.findall(r'(?:^[-+]?)(?:\d+^\s|0b[01][^2-9]+|0x[0-9A-Fa-f]+|0o[0-7][^8-9]+)(?:[^\t\n\r\f\v]$)', text)
    # match = re.findall(r'^[+-]?0b[01][^2-9]+', text)
    print(match)
    if len(match) == 0:
        return None

    if '0b' in match[0] or '0o' in match[0] or '0x' in match[0]:
        print(int(match[0], 0))
        return int(match[0], 0)
    else:
        # print(int(match[0]))
        return int(match[0])


to_integer('123\n')

# ^-?\d+[^\s]$ в начале строки может быть минус(^-?),далее любое количество цифр(\d+),без пробельных символов в конце
# ^-?0b[01]+$ бинарные числа,может быть минус(^-?), индекс бинарного 0b, дибое количество 1 и 0 - [01]
