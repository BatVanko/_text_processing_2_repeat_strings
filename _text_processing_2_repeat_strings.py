words = input().split()
repeat_strings = ""

for word in words:
    word *= len(word)
    repeat_strings += word
print(repeat_strings)
