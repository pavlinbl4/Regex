import re

name = 'Rustle of Wings 1953 Фредерик Браун аудиокнига мистика договор с дьяволом продажа души'


# mask = r'\b[А-Я]{1}[а-я]+\b' # Russian names start with capital letter
# mask = r'\b[а-я]+\b' # Russian names start with low letters
# mask = r'\b\d{4}\b'  # date in name
# mask = r'.+(?= \d{4})'  # all symbol before space and 4 digits
# mask = r'(?<=\d{4}).+'   # all symbol after  4 digits
# mask = r"(?<=\d{4})( \w+)+"   # all symbol after  4 digits
# mask = r"(?<=\d{4} )(\s*\w+\s*)*"
mask = r".+([А-Я]{1}[а-я]+)"


finder = re.search(mask, name)


print(finder.group())
