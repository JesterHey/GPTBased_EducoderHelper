'''
本模块用于定义云端读写的相关操作，包括上传、下载、删除等
'''
import oss2
import os
import json
# 云端存储的文件名称都是shixun_id.json,并且要保证都是有答案的.
# 阿里云 OSS 配置
access_key_id = 'LTAI5t927vdUFZa9NRnWfrL3'
access_key_secret = 'FbXoJUqe545eZhWFvADvGcFwatsGAx'
bucket_name = 'tasks-jsons'
endpoint = 'oss-cn-shenzhen.aliyuncs.com'
# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
# 判断文件是否存在
def is_exist(name:str) -> bool:
    return bucket.object_exists(name)

# 如果文件存在，则下载到本地并命名为shixun_id_answer
def download(name):
    bucket.get_object_to_file(name, f'{name}_answer')
# 上传函数，用于获得答案后上传到云端，此步骤在获得答案后调用
# (to do)如果用户将答案认证为正确，则将本地json中的verified参数改为True后再上传并覆盖云端文件
def upload(name):
    # 上传前先检验文件中的每个键对应的值的answer键是否存在，以及其对应的值是否为空，如果为空，则不上传
    with open(name,'r',encoding='utf-8') as f:
        data = json.load(f)
    for i,j in data.items():
        if 'answer' not in j.keys() or j['answer'] == '':
            # 断言查询结果并抛出异常
            assert False,'答案为空，不予上传'
    bucket.put_object_from_file(name, name)

def delete(name):
    bucket.delete_object(name)

delete('18503.json')