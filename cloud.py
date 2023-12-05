import oss2
import json
import shutil
import os
import get_answer
#获取本地json文件
def get_json(file):
    return [i for i in os.listdir(file) if i.endswith('.json')]
#获取json文件名
json_name = get_json('./')[0]
# 阿里云 OSS 配置
access_key_id = 'LTAI5t927vdUFZa9NRnWfrL3'
access_key_secret = 'FbXoJUqe545eZhWFvADvGcFwatsGAx'
bucket_name = 'tasks-jsons'
endpoint = 'oss-cn-shenzhen.aliyuncs.com'
# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
# 判断文件是否存在
def is_exist(name):
    return bucket.object_exists(name)

exist = is_exist(json_name)
# 如果文件存在，则下载到本地并覆盖本地文件
def download(name):
    bucket.get_object_to_file(name, name)

def upload(name):
    bucket.put_object_from_file(name, name)