import json
with open('18503.json','r',encoding='utf-8') as f:
    data = json.load(f)

for i,j in data.items():
    print(j['answer'])
    print('-'*50)