# 导入LangChain核心提示词模板类
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# 定义示例模板，用于格式化单个示例
example_template = PromptTemplate.from_template("单词:{word},反义词:{antonym}")
# 准备示例数据，包含单词及其反义词
example_data = [{"word": "大", "antonym": "小"}, {"word": "上", "antonym": "下"}]

# 创建Few-Shot提示词模板，组合示例和指令
few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template,  # 单个示例的格式化模板
    examples=example_data,  # 示例数据列表
    prefix="告诉我单词的反义词，我提供了如下示例：",  # 提示词前缀说明
    suffix="基于前面的示例告知我，{input_word}的反义词是：",  # 提示词后缀，包含输入变量
    input_variables=["input_word"]  # 定义输入变量
)
# 调用模板生成提示词，传入具体输入值
prompt_text = few_shot_template.invoke(input={"input_word": "左"}).to_string()
# 输出生成的提示词文本
print(prompt_text)
