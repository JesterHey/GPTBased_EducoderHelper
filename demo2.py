import requests
headers = {
    'Cookie': 'autologin_trustie=bb3a180a619e2e75610e06dcb8181f1951692d36; _educoder_session=497c9154b70e3a840e04f3fba8096472',
    'User-Agent':
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.educoder.net/tasks/27V4D95N/1191512/8p2s3yzoxuit?coursesId=27V4D95N'
}
url = 'https://data.educoder.net/api/myshixuns/gorxjivf6b/challenges.json'
response = requests.get(url=url,headers=headers)
print(len(response.json()))
response.close()