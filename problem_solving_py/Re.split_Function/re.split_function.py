import re

regex_pattern = r"\D+"

print("\n".join(re.split(regex_pattern, input())))
