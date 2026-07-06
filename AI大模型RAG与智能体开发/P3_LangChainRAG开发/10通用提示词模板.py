# 导入langchain库中的核心提示模板模块
from langchain_core.prompts import PromptTemplate

# 导入langchain社区聊天模型中的通义千问模型
from langchain_community.chat_models.tongyi import ChatTongyi

"""
使用LangChain和通义千问模型实现零样本学习命名功能
通过模板化提示，让模型根据姓氏和性别信息生成婴儿名字
"""
# zero-shot
# 创建一个提示模板，用于生成婴儿名字的请求
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender}，你帮我起个名字，简单回答。"
)
# 导入ChatTongyi模型，使用qwen-max版本
# 初始化通义千问聊天模型，指定使用qwen-max版本
model = ChatTongyi(model="qwen-max")
# # 使用模板格式化提示文本，传入姓氏和性别信息
# # 将姓氏设置为"丁"，性别设置为"儿子"，生成具体的提示文本
# prompt_text = prompt_template.format(lastname="丁", gender="儿子")
# # 调用模型获取响应
# # 将格式化后的提示文本发送给模型，获取命名建议
# res = model.invoke(prompt_text)
# # 打印模型返回的结果
# # 输出模型生成的婴儿名字建议
# print(res)
# 调用.format方法注入信息即可
# prompt_text = prompt_template.format(lastname="张", gender="女儿")
#
# model = Tongyi(model="qwen-max")
# res = model.invoke(input=prompt_text)
# print(res)

# 创建一个处理链，将提示模板(model)与模型连接起来
chain = prompt_template | model
#
# 使用链处理输入数据，传入姓氏"丁"和性别"女儿"
res = chain.invoke(input={"lastname": "丁", "gender": "女儿"})
# 打印处理结果
print(res)
