#第8次作业答案在网上
def IsEqual(guess,answer): #定义函数
     if answer > guess:
         print("too big")
         return False
     elif answer < guess:
         print("too small")
         return False
     else:
         return True

from random import randint
f = open('Record.txt')
Record_lines = f.readlines()
f.close()

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

