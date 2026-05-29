from http.client import responses

from openai import OpenAI

client = OpenAI(base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
response = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=[
        {"role": "system", "content": "你是一个Python编程专家，并且不说废话简单回答"},
        {
            "role": "assistant",
            "content": "好的，我是编程专家，并且话不多，你要问什么？",
        },
        {"role": "user", "content": "输出1-10的数字，使用python代码"},
    ],
)
print(response.choices[0].message.content)
