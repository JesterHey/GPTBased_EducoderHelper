import os
import json
#读取当前下的所有以数字命名的json文件
def readJson():
    files = os.listdir()
    jsons = []
    for file in files:
        if file.endswith('.json') and file[0].isdigit():
            jsons.append(file)
    return jsons
#这就是我们的答案json文件，提取每个键盘对应的值的answer键对应的值，写入不同的txt文件
def transToTxt(jsons:list):
    for j in jsons:
        with open(j,'r',encoding='utf-8') as f:
            data = json.load(f)
            i=1
            for key in data.keys():
                if key != 'answer':
                    with open(f'{i}.txt','w',encoding='utf-8') as f:
                        f.write(data[key]['answer'])
                i+=1
            f.close()
if __name__ == '__main__':
    jsons = readJson()
    transToTxt(jsons)