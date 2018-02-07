# -*- coding: utf-8 -*-
#%%
path = '/Users/zhangmimi/Git/SpiderBook/py3/ch1/hello_world.txt'
#%%
# 写
with open(path, 'w') as file:
    file.write('hello, world!')
#%%
# 读
with open(path, 'r') as file:
    contents = file.read()
print(contents)
#%%
# 追加写入
with open(path, 'a') as file:
    file.write('\n' + 'hello, geek!')
    print(contents)
#%%
with open(path, 'r') as file:
    contents = file.readlines()
    print(contents)
#%%
with open(path, 'r') as file:
    while True:
        print(file.readline())
        if not file.readline():
            break
#%%
import json
import pickle

d = dict(url='index.html', title='首页', content='首页')
ob = json.dumps(d, ensure_ascii=False)
print(ob)
ob_p = pickle.dumps(d)
print(ob_p)
print(json.loads(ob))
print(pickle.loads(ob_p))

xlhPath = '/Users/zhangmimi/Git/SpiderBook/py3/ch1/xuliehua.txt'
with open(xlhPath, 'wb') as file:
    pickle.dump(d, file)

with open(xlhPath, 'rb') as file:
    obj_str = pickle.load(file)
    print(obj_str)

with open(xlhPath, 'w') as file:
    json.dump(d, file)

with open(xlhPath, 'r') as file:
    obj_str = json.load(file)
    print(obj_str)