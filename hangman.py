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
    temp = ""
    i = input()
    for w in word:
        if i == w:
            print(i)
            flag = 1
        else:
            temp += w
    word = temp
    if flag != 1:
        pos -= 1
        print(pos)
    flag = 0
    
print("DED")
