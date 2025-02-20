import re


words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]


count_vowel = [(search, len(re.findall(r"[aeiou]", search, re.I))) for search in words]

print(count_vowel)
