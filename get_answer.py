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
#读取当前目录下的json文件
#获得指定目录下的所有json文件的文件名
def get_json(file):
    return [i for i in os.listdir(file) if i.endswith('.json')]
#将file指定为当前目录
file = os.getcwd()
#获得json文件名，因为程序逻辑是每次只有一个json文件，所以直接取第一个
'''
后续准备与云服务器连接，先判断当前json是否已在云服务器上，如果在，则直接调用，
节省调用API的时间和资费，否则，调用API，获得答案，并将答案存入云服务器
阿里云服务器申请成功！
'''
json_name = get_json(file)[0]
#读取json文件并转换为字典
with open(json_name,'r',encoding='utf-8') as f:
    data = json.load(f)
#遍历字典，获得每一关的参数，构造请求，获得答案
'''
用于构造请求的参数：describe,require,code
向GPT提问的格式：promot + 参数模板化的问题
'''
os.environ['http_proxy'] = 'http://127.0.0.1:10809'
os.environ['https_proxy'] = 'http://127.0.0.1:10809'

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
    api_key='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'
)
def get_answer_from_api(jsonfile:dict,client:AsyncOpenAI,promot:str) -> dict:
    data = jsonfile
    client = client
    promot = promot
    # 异步函数来获取答案
    async def get_answer(value):
        des, req, code = value['describe'], value['require'], value['code']
        question = f'问题描述：{des}\n任务需求：{req}\n根据上面的需求，你需要补充并完善代码：\n{code}'
        try:
            response = await client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'system', 'content': promot},
                    {'role': 'user', 'content': question}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f'错误信息：{e}')

    # 主函数
    async def main(data) -> dict:
        tasks = [get_answer(value) for value in list(data.values())[:1:]]
        answers = await asyncio.gather(*tasks)

        # 在data的每个value中新增一个键值对，键为answer，值为答案，并作为返回值返回
        for i,val in enumerate(data.values()):
            val['answer'] = answers[i]

        return data


    # 运行主函数
    return asyncio.run(main(data=data))
new_data = get_answer_from_api(jsonfile=data,client=client,promot=promot)
print(new_data)
#重写本地json文件
with open(json_name,'w',encoding='utf-8') as f:
    json.dump(new_data,f,ensure_ascii=False,indent=4)

