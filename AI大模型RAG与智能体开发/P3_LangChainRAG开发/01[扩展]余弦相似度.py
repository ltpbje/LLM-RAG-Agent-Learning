import numpy as np

"""
计算两个向量的余弦相似度（衡量方向相似性，剔除长度影响）

参数：
    vec_a (np.array): 向量A
    vec_b (np.array): 向量B
返回：
    float: 余弦相似度结果（范围[-1,1]，越接近1方向越一致）
公式：
    cos_sim = (vec_a · vec_b) / (||vec_a|| × ||vec_b||)
    拆解：
    1. 点积：vec_a · vec_b = vec_a[0]×vec_b[0] + vec_a[1]×vec_b[1] + ... + vec_a[n]×vec_b[n]
    2. 模长：||vec_a|| = √(vec_a[0]² + vec_a[1]² + ... + vec_a[n]²)
    3. 模长：||vec_b|| = √(vec_b[0]² + vec_b[1]² + ... + vec_b[n]²)

A: [0.5, 0.5]
B: [0.7, 0.7]
C: [0.7, 0.5]
D: [-0.6, -0.5]
"""


def get_dot(vec_a, vec_b):
    """
    计算两个向量的点积（内积）。

    点积是两个向量对应位置元素乘积的总和，是向量运算中的基础操作，
    常用于计算向量相似度、投影等场景。

    Args:
        vec_a (list[float]): 第一个向量，包含数值类型的列表
        vec_b (list[float]): 第二个向量，包含数值类型的列表

    Returns:
        float: 两个向量的点积结果，即 sum(a_i * b_i) for all i

    Raises:
        ValueError: 当两个向量的维度（长度）不相同时抛出异常
    """
    # 检查两个向量的长度是否相同，不同则无法计算点积
    if len(vec_a) != len(vec_b):
        raise ValueError("2个向量必须维度数量相同")

    # 初始化点积结果为0
    dot_sum = 0
    # 遍历两个向量的对应元素，逐个相乘并累加
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b  # 累加每对元素的乘积

    # 返回最终的点积结果
    return dot_sum


def get_norm(vec):
    """计算单个向量的模长：对向量的每个数字求平方在求和在开根号"""

    sum_square = 0
    for v in vec:
        sum_square += v * v

    # numpy sqrt函数完成开根号
    return np.sqrt(sum_square)


def cosine_similarity(vec_a, vec_b):
    """余弦相似度：2个向量的点积 除以 2个向量模长的乘积"""

    result = get_dot(vec_a, vec_b) / (get_norm(vec_a) * get_norm(vec_b))
    return result


if __name__ == "__main__":
    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]
    vec_c = [0.7, 0.5]
    vec_d = [-0.6, -0.5]

    print("ab:", cosine_similarity(vec_a, vec_b))
    print("ac:", cosine_similarity(vec_a, vec_c))
    print("ad:", cosine_similarity(vec_a, vec_d))
