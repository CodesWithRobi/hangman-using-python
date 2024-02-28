from os import system, name
# clear screen depending on os
def clear():
    system('cls') if name == 'nt' else system('clear')
# mimic the getch() like in C language
def getch():
  import sys, tty, termios
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON
  try:
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch
man = '''
  😀
🫲👕🫱
  👖
  👟👟
'''
man_pos = [17, 16, 15, 8, 7, 6, 4, 0]

s = input()
word = s
flag = 0
pos = 7
clear()
while pos > 0 and len(word) > 0:
    print(man[0:man_pos[pos]])
    print(''.join(['-' if word[i] != '-' else s[i] for i in range(len(word))]))
    i = getch()
    clear()
    count = word.count(i)
    word = word.replace(i, '-')
    if count == 0:
        pos -= 1
    if word.count('-') == len(word):
        print("YOU WON")
        break
if pos == 0:
    print("YOU LOSE")
