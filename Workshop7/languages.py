from programminglanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(python)
print(vb)

list = [ruby, python, vb]

info = ""

for item in list:
    if item.is_dynamic() == True:
        info += item.name + "\n"

print("The dynamically typed languages are:\n" + info)
