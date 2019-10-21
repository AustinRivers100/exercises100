#这篇是自己阅读理解代码用，代码是别处拷贝来的
#第一步把文件读取进来
f = open('scores.txt', encoding='utf-8')
lines = f.readlines()
#print(type(lines),lines) #['刘备 23 35 44 47 51\n', '关羽 60 77 68\n', '张飞 97 99 89 91\n', '诸葛亮 100']
f.close()

results = []
#第二步把从文件得到的字符串转成列表
for line in lines:
    #print (line)  #得到原文件
    data = line.split() #把多余的换行符、空格去掉，
    print (data)  #得到列表，data才是我们真正想要的，到此文件处理完了

    sum = 0
    score_list = data[1:] #对列表切片从第二到列表尾
    for score in score_list:
        sum += int(score)  #各同学成绩求和
    result='%s\t: %d\n' % (data[0], sum)
    #print (result)

    results.append(result)#把结果保存s

#print (results)
output = open('result.txt', 'w', encoding='gbk')
output.writelines(results)
output.close()