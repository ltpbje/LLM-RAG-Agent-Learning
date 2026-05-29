# from langchain_community.llms.tongyi import Tongyi
#
# model = Tongyi(model="qwen-max")
#
# # 通过stream方法获得流式输出
# res = model.stream(input="你是谁呀能做什么？")
#
# for chunk in res:
#     print(chunk, end="", flush=True)

# from langchain_ollama import OllamaLLM
#
# model = OllamaLLM(model="qwen3:4b")
#
# res = model.stream(input="你是谁呀能做什么？")
#
# for chunk in res:
#     print(chunk, end="", flush=True)
#

#
# from langchain_openai import ChatOpenAI
# import os
#
# chatLLM = ChatOpenAI(
#     api_key=os.getenv("DASHSCOPE_API_KEY"),
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
#     model="glm-5.1",  # 此处以qwen-plus为例，您可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
#     # other params...
#     stream_usage=True,
# )
# messages = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "你是谁？"},
# ]
# for chunk in chatLLM.stream(messages):
#     print(chunk.content, end="", flush=True)

# 调用本地模型
from langchain_openai import ChatOpenAI

chatLLM = ChatOpenAI(
    api_key="ollama",  # Ollama 不需要真实 key，随便填即可
    base_url="http://localhost:11434/v1",  # Ollama 本地服务地址
    model="qwen3:8b",  # 替换为你本地已安装的 Ollama 模型名称
    stream_usage=True,
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁？"},
]

for chunk in chatLLM.stream(messages):
    print(chunk.content, end="", flush=True)
