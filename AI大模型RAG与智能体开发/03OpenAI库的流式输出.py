from http.client import responses

from openai import OpenAI

client = OpenAI(base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是一个Python编程专家，并且话很多"},
        {
            "role": "assistant",
            "content": "好的，我是编程专家，并且话很多，你要问什么？",
        },
        {"role": "user", "content": "输出1-10的数字，使用python代码"},
    ],
    stream=True,
)
for chunk in response:
    print(chunk.choices[0].delta.content, end=" ", flush=True)
