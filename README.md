# GPTPowered_EducoderHelper
# 🌟 这是一款由 GPT 构建的头歌作业助手 🚀
>created by JesterHey with 💡
#### 写在前面
首先声明，👩‍💻👨‍💻 本项目适用于**非**图像类编程作业。如果你的作业里有**matplotlib**画图的部分，快去看看[突破！头歌matplotlib相关关卡 100% 通过秘籍](https://github.com/JesterHey/img_file/blob/main/educoder.md)。另外，如你所见，作业助手展现的答案来自于生成式预训练模型(GPT)🤖，但因为评分标准千奇百怪，我们**不能保证**答案的完美无瑕，不过可以给你提供超棒的思路和提示！🌈 当然啦，用了 GPT-4 模型的我们，在处理那些简单题目时，准确度还是杠杠的！👌

## 效果展示📸  

https://github.com/JesterHey/GPTPowered_EducoderHelper/assets/144512889/9311545f-c896-4eac-ab4c-983b682c4a0d  

---


## 前置要求

 1. 谷歌浏览器（Google Chrome）🌐
 2. 装好的谷歌浏览器驱动（ChromeDriver）
 3. Python 版本 3.9 或以上 🐍

如果你还没装谷歌浏览器，快去 [下载一个](https://www.google.com/intl/zh-CN/chrome/) ！
还没下好谷歌浏览器驱动？那就赶紧去 [搞定它](https://googlechromelabs.github.io/chrome-for-testing/) ！
>⚠️注意啦，一定要确保谷歌浏览器和驱动的版本要匹配，否则可能会有意想不到的小插曲哦！

弄好这些之后，就该配置驱动啦！不知道怎么弄的同学可以去 [看看这个](https://www.cnblogs.com/lfri/p/10542797.html)。

## 使用方法
### 1.下载仓库
满足了上面的条件后，选择任意方式下载本仓库📦：

 1. 如果你是 Git 的老手，那就在命令行里直接输入：  
 ```git clone https://github.com/JesterHey/GPTPowered_EducoderHelper.git```  
 下载完毕后，继续输入这个指令：  
 ```pip install -r requirements.txt```

 2. 如果你不太用 Git，那么请下载本项目的压缩包并解压，然后一定要**进入项目的根目录**，就是所有源文件们的那里。确定好了，就在文件夹的空白处右键选择**在终端中打开**，然后输入这个指令：  
  ```pip install -r requirements.txt```
>Mac 或 Linux 用户可能需要这样输入：```pip3 install -r requirements.txt```

### 2.启动程序

上面的步骤都完成后，就在终端里输入：
```python main.py```
>Mac 或 Linux 用户可能得输入：```python3 main.py```

程序启动后，你会看到一个登录页面，就像这样：
 <img src="https://github.com/JesterHey/img_file/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202023-12-09%20211032.png" width = "1000" height = "600" alt="登录页面" align=center />    
 在登录页面的相应位置输入你的头歌账号、密码以及需要获取答案的作业网址（目前只支持**实训作业**和**编程作业**两种类型，其他类型则会提示不支持哦），网址可以选择作业中任意一关的。

### 3.获取答案

程序启动后，会开始爬取和分析作业信息。如果之前有人用过本程序查过这份作业，那么它会直接从服务器下载已经有答案的文件并展示给你；如果还没人查过，那就要调用模型来回答问题了，这可能需要一点时间（5-15秒），具体要看题目的数量和难度。

## 常见问题解答(FAQ)  

 - Q:支持的语言有哪些?
 >理论上GPT会的都支持，但JupyterNotebook除外(题目格式不一样，没做适配🦥)，然后Python的效果最好。
 - Q:加载时间太长/一直显示连接错误？
>首先确保**不要挂代理或者加速器**，其次找个网好点的地方用吧，理论上正常家庭WI-FI速度即可，基本上最长运行时间不会超过5分钟。如果还不行可能就是服务器💥了。  
- Q:出现\[服务器积极拒绝\]错误?
>超过重连次数限制了，关了重开一次
- Q:用这个会被后台检测或者老师看到吗?
>从原理上讲是不会的，本来就只是一个爬虫+GPT，除非你物理贴脸输出🤗。
- Q:能否使用自己的相关密钥构建数据库和选择模型?
>是的，并且推荐使用OSS或者与其类似存储服务，你需要修改**cloud.py**中的相关配置，并先在你的数据库中上传名为apis.json的文件,内容为为\{"my_api":"YOUR_API_KEY"\},你可能需要重写**cloud.py**中的函数逻辑以适配你的服务器上传和下载逻辑。
- Q:考试能用吗?
> 6

## TO DO

 - [ ] 优化UI
 - [ ] 完善用户verified部分
 - [ ] 网页插件版本



## 免责声明 
本工具仅供学习和研究目的使用，使用者需对使用此工具产生的一切后果负责。


