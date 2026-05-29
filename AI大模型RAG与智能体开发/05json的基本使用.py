import json

d = {"name": "周杰轮", "age": 11, "gender": "男"}
# print(json.dumps(d, ensure_ascii=False))

l = [
    {"name": "周杰轮", "age": 11, "gender": "男"},
    {"name": "蔡依林", "age": 12, "gender": "女"},
    {"name": "小明", "age": 16, "gender": "男"},
]
json_str = '{"name": "周杰轮", "age": 11, "gender": "男"}'
json_str_array = '[{"name": "周杰轮", "age": 11, "gender": "男"}, {"name": "蔡依林", "age": 12, "gender": "女"}, {"name": "小明", "age": 16, "gender": "男"}]'
print(json.loads(json_str_array))
print(json.loads(json_str))
