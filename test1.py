import re


def get_strings_before_equal_signs(input_string):
    # 按行分割字符串
    lines = input_string.split('\n')

    # 存储等号左边的字符串
    results = []

    # 正则表达式，匹配等号左边的非空白字符
    pattern = re.compile(r'^\s*(.*?)\s*=')

    for line in lines:
        # 使用正则表达式匹配每一行
        match = pattern.match(line)
        if match:
            # 如果匹配成功，添加匹配的字符串到结果列表
            results.append(match.group(1).strip())

    return results


# 示例字符串，包含多行数据
input_str = """
key1=value1
 key2 = value2
key3=value3
"""

# 调用函数并打印结果
results = get_strings_before_equal_signs(input_str)
print(results)  # 输出: ['key1', 'key2', 'key3']