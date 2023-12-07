'''
主程序：整合各个模块
1、ui文件调用相应ui模块
2、get_params.py获取参数
3、get_answer.py获取答案
4、cloud.py将json文件存入云端
'''

# 生成图形化界面，引导用户登陆并输入实训网址
# 调用get_params.py获取参数，这一步同时隐含了云端获取答案的过程
# 如果云端答案不存在，则调用get_answer.py获取答案，并展示给用户
# 用户verif选项确认后，调用cloud.py将json文件存入云端

# 导入所需模块
import platform
from get_params import get_parameters
from get_answer import get_answer_from_api,promot,client
import json
import os

# 判断当前操作系统
platf = platform.platform()
# 调用login_ui获得用户输入的用户名、密码和实训网址
if platf.startswith('Windows'):
    os.system('python login_ui.py')
else:
    os.system('python3 login_ui.py')

# 检查userinfo.json文件是否存在，存在，则程序继续
assert os.path.exists('userinfo.json'), 'userinfo.json文件不存在,请检查'

# 先读取userinfo.json文件，获得用户名、密码和实训网址
with open('userinfo.json', 'r') as f:
    userinfo = json.load(f)
user_name = userinfo['name']
password = userinfo['pwd']
url = userinfo['url']

# 调用get_params.py获得参数，完成后本地应该有一个json文件，里面有参数
get_parameters(url,user_name,password)
def get_json(file):
    return [i for i in os.listdir(file) if i.endswith('.json')]

#将file指定为当前目录
file = os.getcwd()
json_names = get_json(file)

# 遍历查找以数字开头的json文件，即为获得到的json文件，可能是云端下载的，也可能是爬取的
global j_name
for j in json_names:
    if j[0].isdigit():
        # 将该文件名赋值给json_name
        j_name = j
        break

# 判断json_name文件中是否有answer，若有提取answer并格式化或展现
with open(j_name,'r',encoding='utf-8') as f:
    json_data = json.load(f)
def is_exist_answer(data:dict) -> bool:
    for i,j in data.items():
        if 'answer' in j.keys():
            return True
    return False
if is_exist_answer(json_data):
    pass
else:
    # 调用API获取答案
    new_data = get_answer_from_api(jsonfile=json_data,client=client,promot=promot)
    # 重写本地json文件
    with open(j_name,'w',encoding='utf-8') as f:
        json.dump(new_data,f,ensure_ascii=False,indent=4)

# 上面的判断执行完后，本地的json文件中已经有answer了，下面实现信息展示
# release版本要优化UI，beta版本先用print代替

# 读取json文件，获得answer
with open(j_name,'r',encoding='utf-8') as f:
    data = json.load(f)
# 由于python3.6之后字典是有序的，所以可以直接遍历字典，显示关卡序号和答案
# 要将key在data中对应的索引值+1，因为索引值是从0开始的
for i,j in enumerate(data.items()):
    print(f'第{i+1}关的答案是：{j[-1]["answer"]}')

# 询问用户是否认证答案正确(下午新开一个模块实现)