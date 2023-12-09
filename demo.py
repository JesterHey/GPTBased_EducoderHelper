import os
def getalljsons() -> list:
    return [i for i in os.listdir() if i.endswith('.json')]
for i in getalljsons():
    os.remove(i)