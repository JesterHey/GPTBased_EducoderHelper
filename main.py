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


import login_ui