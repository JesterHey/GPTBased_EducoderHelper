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
from cloud import upload,download,is_exist
print('处理api相关中...')
download('apis.json')
print('处理完成！')
from get_params import get_parameters,get_parameters_of_programming,is_practice
from get_answer import get_shixunanswer_from_api,get_programming_answer_from_api,client,rewrite_programming_json,rewrite_shixun_json
from login_ui import show_login,show_image,MyApp
from trans_to_txt import transToTxt,transToTxt_programming,get_programmingjson,get_shixunjson
import json
import os
from printtxt import print_txt,get_all_txt_file
global finished
finished = False
# 调用login_ui获得用户输入的用户名、密码和实训网址
show_image()
show_login()
promot1 = '实训'
promot2 = '编程'
# 检查userinfo.json文件是否存在，存在，则程序继续
assert os.path.exists('userinfo.json'), 'userinfo.json文件不存在,请检查'

# 先读取userinfo.json文件，获得用户名、密码和实训网址
with open('userinfo.json', 'r') as f:
    userinfo = json.load(f)
user_name = userinfo['name']
password = userinfo['pwd']
url = userinfo['url']
ispractice = is_practice(url=url)
if ispractice:
    # 调用get_params.py获得参数，完成后本地应该有一个json文件，里面有参数
    get_parameters(url,user_name,password)
else:
    get_parameters_of_programming(url=url,user_name=user_name,password=password)
print('参数获取完成！')
# 获得刚才get_params.py生成的json文件名
def is_exist_answer(data:dict) -> bool:
    for i,j in data.items():
        if 'answer' in j.keys():
            return True
    return False
def is_exist_answer_programming(data:dict) -> bool:
    for i in data.keys():
        if i == 'answer':
            continue
        else:
            return False
    return True
if ispractice:
    j_name = get_shixunjson(os.getcwd())[0]
    # 判断j_name文件中是否有answer
    with open(j_name,'r',encoding='utf-8') as f:
        json_data = json.load(f)
    if is_exist_answer(json_data):
        pass
    else:
        print('调用api获取答案中，请耐心等待...')
        new_data = get_shixunanswer_from_api(jsonfile=json_data,client=client,promot=promot1)
        # 重写本地json文件
        rewrite_shixun_json(json_name=j_name,new_data=new_data)
else:
    j_names = get_programmingjson(os.getcwd())
    # 判断是否有answer
    for j in j_names:
        with open(j,'r',encoding='utf-8') as f1:
            j_data = json.load(f1)
        if not is_exist_answer_programming(j_data):
            break
    print('调用api获取答案中，请耐心等待...')
    new_data = get_programming_answer_from_api(jsonfile=j_names,client=client,promot=promot2)
    # 重写本地接送文件
    rewrite_programming_json(json_names=j_names,new_data=new_data)

# 上面的判断执行完后，本地的json文件中已经有answer了，下面实现信息展示
# 先删除本地api.json文件
os.remove('apis.json')
# 函数读取当前目录下的所有json文件
if ispractice:
    JSS = get_shixunjson(os.getcwd())[0]
    # 构建txt文件
    transToTxt(JSS)
    # 展示txt文件
    # 判断云端是否存在答案json，如果不存在，则上传
    print('答案获取完毕，开始展示')
    print_txt(get_all_txt_file(os.getcwd()))
    if not is_exist(JSS):
        print('开始上传答案到云端,请勿关闭程序')
        upload(JSS)
        print('上传完毕')
else:
    JSS = get_programmingjson(os.getcwd())
    transToTxt_programming(JSS)
    print('答案获取完毕，开始展示')
    print_txt(get_all_txt_file(os.getcwd()))
    for i in JSS:
        if not is_exist(i):
            print('开始上传答案到云端,请勿关闭程序')
            upload(i)
            print('上传完毕')
# #打印完，删除本地txt和json文件
def getalljsons() -> list:
    return [i for i in os.listdir() if i.endswith('.json')]
for i in getalljsons():
    os.remove(i)
# 删除本地所有数字命名的txt文件
for i in os.listdir():
    if i.split('.')[0].isdigit() or i.startswith('pro') and i.endswith('.txt'):
        os.remove(i)
