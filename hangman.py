print('''
  😀
🫲👕🫱
  👖
  👟👟
''')
s = input()
word = s
flag = 0
pos = 8
while pos > 1 and len(word) > 0:
    i = input()
    count = word.count(i)
    word = word.replace(i, '-')
    for i in range(len(word)):
        if s[i] == word[i]:
            print('-', end='')
        else:
            print(s[i], end='')
    print()
    if count == 0:
        pos -= 1
        print(pos)
print("DED")
