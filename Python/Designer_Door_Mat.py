values = input()
line, colun = values.split()
line = int(line)
colun = int(colun)

l = '---'
welcome = '-WELCOME-'
meadle = '.|.'

times = line // 2
start = 1

for i in range(1, line + 1):
    if i == line // 2 + 1:
        print(f'{l * (line // 2 -1)}{welcome}{l * (line // 2 -1)}')
    if i <= line // 2:
        print(f'{l * times}{meadle * start}{l * times}')
        times -= 1
        start += 2
    if i == line // 2 + 2:
        start -= 2
        times = 1
    if i > line // 2 + 1:
        print(f'{l * times}{meadle * start}{l * times}')
        times += 1
        start -= 2
        