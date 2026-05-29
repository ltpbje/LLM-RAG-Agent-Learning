from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 配置本地Ollama模型
model = ChatOpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # Ollama本地服务地址
    model="glm-5.1",  # 替换为你本地已安装的Ollama模型名称
    stream_usage=True,
)

# 准备消息列表
messages = [
    # (角色，内容)  角色：system/human/ai
    ("system", "你是一个边塞诗人。"),
    ("human", "写一首唐诗。"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    ("human", "按照你上一个回复的格式，在写一首唐诗。"),
]

# 调用stream流式执行
res = model.stream(messages)

# for循环迭代打印输出，通过.content来获取到内容
for chunk in res:
    print(chunk.content, end="", flush=True)
