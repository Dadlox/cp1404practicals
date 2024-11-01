"""
Codes: programming_language.py and languages.py
Coder: Hein Htet
Started at: 10:30
Ended: 11:14
"""
from Codes.Practical.Week6.prac_06.languages import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
languages = [python,ruby,visual_basic]

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)