from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
man = '''
  😀
🫲👕🫱
  👖
  👟👟
'''
s = input()
word = s
flag = 0
pos = 8
while pos > 1 and len(word) > 0:
    i = input()
    clear()
    count = word.count(i)
    word = word.replace(i, '-')
    print(''.join(['-' if word[i] != '-' else s[i] for i in range(len(word))]))
    print()
    if count == 0:
        pos -= 1
        print(pos)
print("DED")
