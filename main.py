from file import *

f = SimpleFile(r"D:\self\SimpleFile\SimpleFile\sample.txt")
print(f.read_first_char())
print(f.read_first_char())
print(f.read_first_char())
print(f.read_first_word(tmp=False))
print(f.read_first_char())
print(f.read_first_sentence(contain_ender=False))
print(f.read_first_sentence(contain_ender=True))
print(f.read_first_paragraph(tmp=False,contain_ender=True))
print(f.read_first_word())