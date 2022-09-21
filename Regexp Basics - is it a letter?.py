import re

def is_letter(s):
    return bool(re.match(r'[a-zA-Z]{1}\Z',s))


print(is_letter('R '))