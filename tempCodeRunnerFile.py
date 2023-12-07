'''
# 主程序：整合各个模块
# 1、ui文件调用相应ui模块
# 2、get_params.py获取参数
# 3、get_answer.py获取答案
# 4、cloud.py将json文件存入云端
# '''
# # 生成图形化界面，引导用户登陆并输入实训网址
# # 调用get_params.py获取参数，这一步同时隐含了云端获取答案的过程
# # 如果云端答案不存在，则调用get_answer.py获取答案，并展示给用户
# # 用户verif选项确认后，调用cloud.py将json文件存入云端

# # 导入所需模块

# from get_params import get_parameters
# from get_answer import get_answer_from_api,promot,client
# from login_ui import show_login,show_image,MyApp
# from trans_to_txt import transToTxt,readJson

# import json
# import os

# # 调用login_ui获得用户输入的用户名、密码和实训网址
# show_image()
# show_login()

# # 检查userinfo.json文件是否存在，存在，则程序继续
# assert os.path.exists('userinfo.json'), 'userinfo.json文件不存在,请检查'

# # 先读取userinfo.json文件，获得用户名、密码和实训网址
# with open('userinfo.json', 'r') as f:
#     userinfo = json.load(f)
# user_name = userinfo['name']
# password = userinfo['pwd']
# url = userinfo['url']

# # 调用get_params.py获得参数，完成后本地应该有一个json文件，里面有参数
# get_parameters(url,user_name,password)

# # 获得本地所有数字开头的json文件名
# j_name = readJson()[0]
# # 判断j_name文件中是否有answer
# with open(j_name,'r',encoding='utf-8') as f:
#     json_data = json.load(f)

# def is_exist_answer(data:dict) -> bool:
#     for i,j in data.items():
#         if 'answer' in j.keys():
#             return True
#     return False

# if is_exist_answer(json_data):
#     pass
# else:
#     # 调用API获取答案
#     new_data = get_answer_from_api(jsonfile=json_data,client=client,promot=promot)
#     # 重写本地json文件
#     with open(j_name,'w',encoding='utf-8') as f:
#         json.dump(new_data,f,ensure_ascii=False,indent=4)

# # 上面的判断执行完后，本地的json文件中已经有answer了，下面实现信息展示
# # 使用readJson函数读取当前目录下的所有json文件
# JSONS = readJson() 
# # 构建txt文件
# # transToTxt(JSONS)
# # 展示txt文件