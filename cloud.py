import oss2
import json
import shutil
import os
import get_answer
#获取本地json文件
def get_json(file):
    return [i for i in os.listdir(file) if i.endswith('.json')]
json_name = get_json(os.getcwd())[0]
# 阿里云 OSS 配置
access_key_id = 'LTAI5t927vdUFZa9NRnWfrL3'
access_key_secret = 'FbXoJUqe545eZhWFvADvGcFwatsGAx'
bucket_name = 'tasks-jsons'
endpoint = ''
# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
# 判断文件是否存在
exist = bucket.object_exists(json_name)
# 如果文件存在，则下载到本地并覆盖本地文件
if exist:
    bucket.get_object_to_file(json_name, json_name)
    print('已从云服务器下载文件')
else: #否则调用OpenAI API获得答案，并上传到云服务器
    new_data = get_answer.new_data
    #将new_data变为json格式并上传到云端
    with open(json_name, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
    bucket.put_object_to_file(json_name,json_name)
