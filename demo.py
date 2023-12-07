import json
with open('demo.json','r',encoding='utf-8') as f:
    data = json.load(f)
for i,j in enumerate(data.items()):
    print(i,j[-1])