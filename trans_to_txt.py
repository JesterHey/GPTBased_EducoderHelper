import os
import json
def get_shixunjson(file:str) -> list:
    '''
    file:文件夹路径
    '''
    files = os.listdir(file)
    jsonfiles = []
    for i in files:
        if i.endswith('.json') and i[0].isdigit():
            jsonfiles.append(i)
    return jsonfiles
#获得指定目录下的所有pro开头的json文件
def get_programmingjson(file:str) -> list:
    '''
    file:文件夹路径
    '''
    files = os.listdir(file)
    jsonfiles = []
    for i in files:
        if i.endswith('.json') and i.startswith('pro'):
            jsonfiles.append(i)
    return jsonfiles
def transToTxt(jsons:list):
    '''
    用于将jsons中的所有json中的answer信息写入txt
    '''
    for j in jsons:
        with open(j,'r',encoding='utf-8') as f1:
            data = json.load(f1)
            i=1
            for key in data.keys():
                if key != 'answer':
                    with open(f'{i}.txt','w',encoding='utf-8') as f2:
                        f2.write(data[key]['answer'])
                i+=1

def transToTxt_programming(jsons:list):
    for j in range(len(jsons)):
        with open(jsons[j],'r',encoding='utf-8') as f1:
            data = json.load(f1)
            with open(f'{j+1}.txt','w',encoding='utf-8') as f2 :
                f2.write(data['answer'])


if __name__ == '__main__':
    print('测试部分')
    # jsons = get_shixunjson(os.getcwd())
    # transToTxt(jsons)
    jsons  = get_shixunjson(os.getcwd())
    print(jsons)
    transToTxt(jsons)
