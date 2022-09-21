import re

pattern = r'(\d[02]-\d[1-28])|(\d[01,3,5,7,8,10,12]-\d[1-31])|(\d[4,6,9,11]-\d[1-30])'
text = "[02-31]"

match = re.compile(pattern,text)
print(match)