import re

file_name = "Dodkin Job 1959.mp4"

mask = r'\.mp4'

print(re.search(mask, file_name))
