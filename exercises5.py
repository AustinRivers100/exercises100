#第五次作业
from random import randint
print("Here is a game to guess a number,and it's from 1 to 100.")
username = input('The frist, please Enter your name:')
print('Hello', username ,",Let's go ")
total_Rounds = 0  #总次数
total_times = 0   #总轮数
Thefastest_Round = 50  #最快一轮

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
            print("You have guessed %d times."%(time))
            break
    if Thefastest_Round>time:
        Thefastest_Round = time
    print("You have played %d Rounds,try for %d times,average %.2f per Round,fastest try is %d." % (total_Rounds, total_times, total_times/total_Rounds,Thefastest_Round ))
    tips = input("'y' key to Continue,else to EXIT")
    if tips != str('y'):
        print("see you next!")
        break
Record = 'username: %s; total_Rounds: %d ;total_times: %d; Thefastest_Round: %d; average: %.2f' %(username,total_Rounds,total_times,Thefastest_Round,total_times/ total_Rounds)
F = open('Record.txt','w')
F.write(Record)
F.close()