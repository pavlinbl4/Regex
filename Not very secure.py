import re

def alphanumeric(password):
    return bool(re.findall(r'^[^\W]+$',password))

print(alphanumeric('PassW0rd'))