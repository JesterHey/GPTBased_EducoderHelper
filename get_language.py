from trans_to_txt import get_shixunjson, get_programmingjson
import os
import json
shixuns = get_shixunjson(os.getcwd())
programmings = get_programmingjson(os.getcwd())
def get_shixun_language(shixuns:list) -> list:
    '''
    用于获得所有实训的语言
    '''
    languages = []
    for i in shixuns:
        with open(i,'r',encoding='utf-8') as f:
            data = json.load(f)
            for j in data.keys():
                if j != 'answer':
                    languages.append(data[j]['language'])
    return languages

def get_programming_language(programmings:list) -> list:
    '''
    用于获得所有编程题的语言
    '''
    languages = []
    for i in programmings:
        with open(i,'r',encoding='utf-8') as f:
            data = json.load(f)
            languages.append(data['language'])
    return languages


if __name__ == '__main__':
    if shixuns == []:
        language_result = get_programming_language(programmings)
        print(language_result)
    elif programmings == []:
        language_result = get_shixun_language(shixuns)
        print(language_result)