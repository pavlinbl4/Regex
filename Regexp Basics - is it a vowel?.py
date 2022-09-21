import re




def vowel(text):
    rr = re.findall(r'^[aeiou]{1}[^\s]$', text, re.IGNORECASE)
    return rr


print(vowel('o\n'))
