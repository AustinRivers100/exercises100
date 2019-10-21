#第6次作业记录自己最好的成绩
#step1 把文本文件读取进来
from random import randint
f = open('Record.txt') #打开文件
lines = f.read() #把文件内容读取进来得到一个字符串
#print(type(lines), lines ) #读取完成
f.close()
#step2 因为读进来的是一个字符串，需要处理成可以直接使用的数据，即字符串 -> 列表
data = lines.split() #lines还是lines,列表data才是我们想要的
#print(data)
#step3 把自己上回的游戏数据代入各个初始值
name = input('what is your name:')
print('Hello', username, "welcome back ")
total_Rounds = int(data[1])
total_times = int(data[2])
Thefastest_Round = int(data[3])

while True:
    total_Rounds += 1  #重新开始游戏，总轮数+1次，所以要放在这行
    time = 0           #这是内层循环的变量，初始值放这里
    guess = randint(1,100) #重新开始游戏，随机数变化1次

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
    if Thefastest_Round>time:
        Thefastest_Round = time
    print("You have played %d Rounds,try for %d times,average %.2f per Round,fastest try is %d." % (total_Rounds, total_times, total_times/total_Rounds,Thefastest_Round ))
    tips = input("'y' key to Continue,else to EXIT")
    if tips != str('y'):
        print("see you next!")
        break
Record = ' %s %d %d %d ' %(username,total_Rounds,total_times,Thefastest_Round)
F = open('Record.txt','w')
F.write(Record)
F.close()
