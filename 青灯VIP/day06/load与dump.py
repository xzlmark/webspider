import json

# 如果要将中文写入文件中，则需要指定ensure_ascii=False
with open('test.json','a',encoding='utf-8') as f:
    json.dump('熊珍龙', f,ensure_ascii=False)  # 写入，序列化


# 如果要将json文件中的中文输出，则必须通过下面的方式获取
# with open('test.json',encoding='utf-8') as f:
#     text = json.load(f)
#     print(text)