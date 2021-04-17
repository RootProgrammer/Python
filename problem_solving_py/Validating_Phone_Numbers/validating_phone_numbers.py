import re

checkPhoneNumber = ["YES" if re.match(
    "^[789]{1}\d{9}$", input()) else "NO" for _ in range(int(input()))]

print("\n".join(checkPhoneNumber))
