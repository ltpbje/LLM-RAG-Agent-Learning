from http.client import responses

from openai import OpenAI

client = OpenAI(base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是AI助理，回答很简洁"},
        {"role": "user", "content": "小明有2条宠物狗"},
        {
            "role": "assistant",
            "content": "好的",
        },
        {"role": "user", "content": "小红有3只宠物猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有几个宠物?"},
    ],
    stream=True,
)
for chunk in response:
    print(chunk.choices[0].delta.content, end=" ", flush=True)
