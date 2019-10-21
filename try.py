import random
f = open('Record.txt')
data_lists = f.readlines()
f.close()
data = {}
for i in data_lists:
    scores = i.split()
    data[scores[0]] = scores[1:]
name = input('请输入你的用户名：')
score = data.get(name)

if score is None:
    score = [0,0,0]

game_times = int(score[0])
total_times = int(score[1])
speed_times = int(score[2])

if game_times > 0:
    avg_times = total_times/game_times
else:
    avg_times = 0

print('嗨 %s，你上回玩了%d次，总玩了%d轮，最快%d轮猜中，平均%d轮猜中'
% (name, game_times, total_times, speed_times, avg_times))

while True:
    num = random.randint(1,10)
    count = 0
    print('------------第%d次，本次游戏开始了---------' % game_times)
    while True:
        count += 1
        while True:
            try:
                ans = int(input('请输入你猜的数字：'))
                break
            except ValueError:
                print('你输入的不是数字 请重新输入')
        if ans > num:
            print('这是第%d轮，你猜的数字是%d，太大了' % (count,ans))
        elif ans < num:
            print('这是第%d轮，你猜的数字是%d，太小了' % (count,ans))
        else:
            print('这是第%d轮，你猜的数字是%d，猜对了 恭喜！' % (count,ans))
            break
    if game_times == 0 or count < speed_times:
        speed_times = count
        print('-------------------------------')
        print('---这是最快纪录，第%d轮猜中！---' % speed_times)
        print('-------------------------------')
    game_times += 1
    total_times += count
    avg_times = total_times/game_times
    print('你玩了总共%d次，总共%d轮，最快猜中%d轮，平均猜中%.2f轮' %
    (game_times, total_times, speed_times, avg_times))

    jixu = input('按任意键继续游戏，回车退出！')
    if not jixu:
        print('游戏退出成功，欢迎再来！')
        break

data[name] = [str(game_times),str(total_times),str(speed_times)]
result = ''
for n in data:
    line = n + ' ' + ' '.join(data[n])+ '\n'
    result += line
f = open('Record.txt', 'w', encoding='utf-8')
f.write(result)
f.close
