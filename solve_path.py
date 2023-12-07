'''
本模块用于解决macOS和Windows路径格式问题
'''
import os
# 获取当前脚本所在的目录
current_directory = os.path.dirname(os.path.abspath(__file__))
# 拼接完整路径
picture_folder_path = os.path.join(current_directory, 'picture')
# 获取所有文件
all_files = os.listdir(picture_folder_path)
# 筛选以a.png和b.png结尾的文件
target_files = [file for file in all_files if file.endswith(('b2.png', 'b2txt.png'))]
# 获取完整路径
file_paths = [os.path.join(picture_folder_path, file) for file in target_files]
# 打印文件路径
b2_path = ''
b2txt_path = ''
for file_path in file_paths:
    if file_path.endswith('b2.png'):
        b2_path = file_path
    else:
        b2txt_path = file_path

if __name__ == '__main__':
    print(b2_path)
    print(b2txt_path)
    print(os.listdir(current_directory))