import re

def hapax(filepath):
    file = open(filepath,encoding='utf-8')
    words = re.findall('\w+', file.read().lower())
    frequencies = {k: 0 for k in words}
    for word in words:
        frequencies[word] += 1

    for word in frequencies:
        if frequencies[word] == 1:
            print(word)


hapax(r"C:\CS stuff\Assignments-Repository\LEC HW\Programming exercises (file)\gutenberg.txt")