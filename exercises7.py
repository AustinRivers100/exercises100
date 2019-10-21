#第7次作业记录请朋友来玩
#step1 把文本文件读取进来
from random import randint
f = open('Record.txt') #打开文件
Record_lines = f.readlines() #用readlines把文件内容按行读取进来得到一个列表
#print(type(Record_lines), Record_lines ) #可以查看下处理效果
f.close()
#step2 因为读进来的是一个包含多项字符串的列表，需要还处理成可以直接使用的数据
game_dict = {}
for i in Record_lines:
    Record = i.split()#去处空白符
    #print(Record )
    game_dict[Record[0]] = Record[1:] #给字典赋值
    #print (game_dict)
name = input('what is your name:')
players_name = game_dict.get(name) #如果用户在字典里，直接获取对应玩家游戏数据
if players_name is None:
    players_name = [0,0,0]#如果是新用户，则各项数据初始化
total_Rounds = int(players_name[0])
total_times = int(players_name[1])
Thefastest_Round = int(players_name[2])
#print(players_name) #查看下处理效果
print('Welcome',name, ",In Last Record,You have played %d Rounds,try for %d times,fastest try is %d." % (total_Rounds, total_times,Thefastest_Round ))
while True:
    total_Rounds += 1  #重新开始游戏，总轮数+1次，所以要放在这行
    time = 0           #这是内层循环的变量，初始值放这里
    guess = randint(1,10) #重新开始游戏，随机数变化1次

    while True:
        answer = int(input(" What is your guess: "))
        time +=1    #每次游戏的轮数，猜一次就记录一次，所以要放在这一行
        total_times += 1 #猜一次，轮数加1次
        if answer > guess:
            print( "too big")
        elif answer < guess:
            print( "too small")
        else:
            print("Oh,that's great,you did it!")
            print("IN this round,you have guessed %d times."%(time))
            break
    if Thefastest_Round>time or Thefastest_Round == 0: #求最快值，最快不可能是0，所以。。。
        Thefastest_Round = time

    print("You have played %d Rounds,try for %d times,fastest try is %d." % (total_Rounds, total_times,Thefastest_Round ))
    tips = input("'y' key to Continue,else to EXIT")
    if tips != str('y'):
        print("see you next!")
        break
##step3写入数据保存
game_dict[name] = [str(total_Rounds),str(total_times),str(Thefastest_Round)]
new_data = ''
for j in game_dict:
    line = j + ' ' + ' '.join(game_dict[j])+ '\n'

    new_data += line
F = open('Record.txt','w')
F.write(new_data)
F.close()

