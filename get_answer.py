'''
本模块用于答案获得
1、先获得本地的json文件
2、云端检查json是否存在，存在则直接调用，不存在则步骤3
3、调用openai的api获得答案并处理格式，生成新的json文件并存储在云端
'''
from openai import AsyncOpenAI
import os
import json
import asyncio
from cloud import download,delete
import base64
#读取当前目录下的json文件
#获得指定目录下的所有数字开头的json文件的文件名
def get_json(file:str) -> list:
    '''
    file:指定目录
    '''
    return [i for i in os.listdir(file) if i.endswith('.json') and i[0].isdigit()]
#获得json文件名，因为程序逻辑是每次只有一个json文件，所以直接取第一个
'''
与云服务器连接，先判断当前json是否已在云服务器上，如果在，则直接调用，
节省调用API的时间和资费，否则，调用API，获得答案，并将答案存入云服务器

12.4晚更新：
阿里云服务器申请成功！
'''
# 以下封装成函数
#读取json文件并转换为字典
def load_json_data(json_name:str) -> dict: 
    with open(json_name,'r',encoding='utf-8') as f: # json_name为无答案的json文件名
        data = json.load(f)
    return data
def load_api_key() -> str:
    with open('apis.json','r',encoding='utf-8') as f: # apis.json为存储api_key的json文件名
        return json.load(f)['openaiapi']

#遍历字典，获得每一关的参数，构造请求，获得答案
'''
用于构造请求的参数：describe,require,code
向GPT提问的格式：promot + 参数模板化的问题
'''

promot = '现在，我想让你扮演一个Python程序员来解一个问题，我的问题将由三个部分组成，第一部分是问题的描述，第二部分是问题的需求，第三部分是问题的代码，我需要你按照我的模板编写代码。并且你返回的代码应当是带有注释的'
#构造问题模板
#遍历字典，获得每一关的参数，构造请求，获得答案
#使用异步函数提升效率
'''
异步思路：由于每一关都会的答案查询都是独立的，可以把不同的查询请求构建成异步任务，谁先完成就先返回谁的答案，
最后把所有的答案整合到一个字典中，再写入json文件中
'''

# 初始化异步客户端
client = AsyncOpenAI(
    api_key=load_api_key(),
    base_url='https://api.op-enai.com/v1'
)
def get_answer_from_api(jsonfile:dict,client:AsyncOpenAI,promot:str) -> dict:
    '''
    jsonfile:本地json文件
    client:异步客户端
    promot:问题模板
    '''
    data = jsonfile
    client = client
    promot = promot
    # 异步函数来获取答案
    async def get_answer(key,value) -> str:
        cid = key
        # code 是base64编码的字符串，需要解码
        des, req, code = value['describe'], value['require'], base64.b64decode(value['code']).decode('utf-8')
        question = f'问题描述：{des}\n任务需求：{req}\n根据上面的需求，你需要补充并完善代码：\n{code}'
        try:
            response = await client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'system', 'content': promot},
                    {'role': 'user', 'content': question}
                ]
            )
            return f'{cid}/{response.choices[0].message.content}'
        except Exception as e:
            print(f'错误信息：{e}')

    # 主函数
    async def main(data) -> dict:
        ansewer_data = data
        tasks = [get_answer(cid,value) for cid,value in data.items()]
        answers = await asyncio.gather(*tasks) # 返回一个列表，列表中的每个元素为每个异步任务的返回值
        #由于异步获得的答案顺序不确定，需要处理,先把答案按照关卡id排序
        answers = sorted(answers,key=lambda x:int(x.split('/')[0]))
        # 在data的每个value中新增一个键值对，键为answer，值为答案，并作为返回值返回
        for i in range(len(answers)):
            ansewer_data[list(ansewer_data.keys())[i]]['answer'] = answers[i].split('/')[-1]

        return ansewer_data


    # 运行主函数
    return asyncio.run(main(data=data))
if __name__ == '__main__':
    new_data = get_answer_from_api(jsonfile=load_json_data(get_json(os.getcwd())[0]),client=client,promot=promot)
    print(new_data)
    #重写本地json文件
    with open(get_json(os.getcwd())[0],'w',encoding='utf-8') as f:
        json.dump(new_data,f,ensure_ascii=False,indent=4)

