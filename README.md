# Test





## workflow

主问题划分为固定类别的子问题（可能需要迭代划分）、子问题分类、调用工具解决子问题、将子问题的答案聚合（可能需要迭代）



主问题划分为多个子问题，分别可以通过查询一下四个数据表解决。公司基本信息表，公司注册信息表，上市公司子公司关联信息表，法律文书信息表。



智谱GLM-4接口请求参数中的tool

接口文档：https://open.bigmodel.cn/dev/api#glm-4

<img src="fig\tool.png" alt="tool" style="zoom:50%;" />



智谱ChatGLM系列的函数调用介绍：

https://open.bigmodel.cn/dev/howuse/functioncall

tools 是内容生成 API 中的可选参数，用于向模型提供函数定义。通过此参数，模型能够生成符合用户所提供规范的函数参数。请注意，**API 实际上不会执行任何函数调用，仅返回调用函数所需要的参数**。开发者可以利用模型输出的参数在应用中执行函数调用。 







































