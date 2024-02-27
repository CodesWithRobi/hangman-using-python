print('''
  😀
🫲👕🫱
  👖
  👟👟
''')
word = input()
flag = 0
pos = 8
while pos > 1 and len(word) > 0:
    i = input()
    count = word.count(i)
    word = word.replace(i, '')
    print(word)
    if count == 0:
        pos -= 1
        print(pos)
print("DED")
