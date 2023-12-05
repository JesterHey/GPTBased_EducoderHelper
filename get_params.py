'''
本模块用于获取作业的参数，包括：
1、关卡数
2、每关的参数
    a:任务描述
    b:编程要求
    c:编辑器中的所有代码
3、课程id,实训id
4、写入本地json文件中
'''

#导入所需模块
import json
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
from lxml import etree
import time
import requests
from cloud import is_exist,download,upload
#配置参数
opt = Options()
opt.add_experimental_option('detach', True)
chrome_driver = 'D:\ChromeDownload\chromedriver-win64\chromedriver-win64'
#以下部分在发行版本需要优化UI
# url = input('请输入作业中任意一关的网址：')
# user_name = input('请输入用户名：')
# password = input('请输入密码：')
url = 'https://www.educoder.net/tasks/27V4D95N/1191515/vmxpzae734bj?coursesId=27V4D95N'
user_name = 'hnu202311020126'
password = 'hzy123456'
# 另外，目前好像只有实训作业有这些参数，其他的作业例如编程作业就没有，所以先判断一下是否为实训作业，可以通过用户输入的url判断
# 主要是看educoder.net/后面是否有tasks，如果有，则是实训作业，否则，不是实训作业
def is_practice(url):
    obj=re.compile(r'www.educoder.net/tasks')
    if obj.search(url):
        return True
    else:
        return False
if is_practice(url):
    #构造selenium对象
    safari = Chrome()
    safari.get(url)
    #模拟登录
    safari.implicitly_wait(10)
    safari.find_element(By.ID, 'login').send_keys(user_name)
    safari.find_element(By.ID, 'password').send_keys(password)
    safari.find_element(By.ID, 'password').send_keys(Keys.ENTER)
    time.sleep(2)
    #获取cookie，User-Agent
    Cookie = safari.get_cookies()
    User_Agent = safari.execute_script('return navigator.userAgent')
    cookie = f'autologin_trustie={Cookie[1]["value"]}; _educoder_session={Cookie[0]["value"]}'
    #先获取到shixun_id便于先判断云端文件是否存在
    cur_url = url
    identity = cur_url.split('/')[-1].split('?')[0]
    id_url = f'https://data.educoder.net/api/tasks/{identity}.json?'
    headers = {
        'Cookie':cookie,
        'User-Agent':User_Agent,
        'Referer':cur_url
    }
    response = requests.get(url=id_url, headers=headers)
    shixun_id = dict(response.json())['challenge']['shixun_id']
    #判断云端文件是否存在
    exist = is_exist(f'{shixun_id}.json')
    if exist: #存在，则跳转到云端下载并终止本程序
        print('云端文件已存在，正在下载')
        download(f'{shixun_id}.json')
        safari.close()
        exit()
    else: #不存在，则继续执行本程序
        print('云端文件不存在，开始获取参数')
        #获取关卡数
        #点击展开关卡页面
        safari.find_element(By.XPATH,'//*[@id="task-left-panel"]/div[1]/a[1]').click()
        time.sleep(2)
        #关卡数量由 class = "flex-container challenge-title space-between" 的元素数量决定
        htmltxt = safari.page_source
        html = etree.HTML(htmltxt)
        task_num = html.xpath('count(//*[@class="flex-container challenge-title space-between"])')
        task_num = int(task_num)
        #关闭关卡页面
        safari.find_element(By.XPATH,'//*[@id="task-left-panel"]/div[3]/div[1]').click()
        #对于每一关，获取参数
        #每一关的参数由以下元素组成：
        '''
        /html/body/div[1]/div/div/div/div[2]/section[1]/div[3]/div[3]/div/div/div/div/div[3]/div[1]/a
        /html/body/div[1]/div/div/div/div[2]/section[1]/div[3]/div[3]/div/div/div/div/div[4]/div[1]/a
        '''
        obj1 = re.compile(r'<h3 id="任务描述">任务描述</h3><p>(?P<describe>.*?)</p>',re.S)
        obj2 = re.compile(r'<h3 id="编程要求">编程要求</h3><p>(?P<require>.*?)</p>',re.S)
        #初始化一个总的json文件，名称为课程的id
        total = {}
        #另外，目前好像只有实训作业有这些参数，其他的作业例如编程作业就没有，所以先判断一下是否为实训作业
        # def is_practice():
        #     try:
        #         safari.find_element(By.XPATH,'//*[@id="task-left-panel"]/div[1]/a[1]')
        #         return True
        #     except BaseException:
        #         return False
        i=1
        try:
            while i <= task_num:
                safari.implicitly_wait(10)
                safari.find_element(By.XPATH, '//*[@id="task-left-panel"]/div[1]/a[1]').click()
                safari.implicitly_wait(10)
                safari.find_element(By.XPATH,f'/html/body/div[1]/div/div/div/div[2]/section[1]/div[3]/div[3]/div/div/div/div/div[{i}]/div[1]/a').click()
                time.sleep(3)
                #获取课程id -> 根据url中?前面的，最后一个/后面的那部分参数构造请求，同时，似乎还需要用到cookie，User-Agent和Referer参数，这些统一用selenium在登陆后获取并组装成headers
                #获取cookie，User-Agent和Referer
                cur_url=Referer = safari.current_url
                identity = cur_url.split('/')[-1].split('?')[0]
                id_url = f'https://data.educoder.net/api/tasks/{identity}.json?'
                #获取课程id
                headers = {
                    'Cookie':cookie,
                    'User-Agent':User_Agent,
                    'Referer':Referer
                }
                try:
                    response = requests.get(url=id_url,headers=headers)
                    challenge_id = dict(response.json())['challenge']['id']
                    shixun_id = dict(response.json())['challenge']['shixun_id']
                except BaseException:
                    print('获取课程id失败')
                #获取任务描述(如果存在的话)
                page_source = safari.page_source
                describe = obj1.findall(page_source)
                #获取编程要求(如果存在的话)
                require = obj2.findall(page_source)
                #获取编辑器中的代码,由于代码都是class = "view-line"的div,先找到所有class = "view-line"的div，获取其中的所有文本，再把不同行的代码用\n连接起来
                code = safari.find_elements(By.CLASS_NAME,'view-line')
                code = '\n'.join([i.text for i in code]).lstrip('\n')
                #把参数存入字典，再转换为json格式
                task = {
                    'describe':describe[0] if len(describe) != 0 else '',
                    'require':require[0] if len(require) != 0 else '',
                    'code':code,
                    'verified': False #这个参数是用来标记答案是否被用户认证为正确答案的，初始值为False
                }
                #把每一关的参数存入总的字典中
                total[challenge_id] = task
                #去往下一关
                i += 1
        except BaseException:
            print('获取参数失败')
        #把参数写入本地json文件中，文件名字与shixun_name相同键为course_id，值为一个列表，列表中每个元素为一个字典，字典中包含每一关的参数
        with open(f'{shixun_id}.json','w',encoding='utf-8') as f:
            json.dump(total,f,ensure_ascii=False,indent=4)
else:
    print('这不是一个实训作业')
    exit()
