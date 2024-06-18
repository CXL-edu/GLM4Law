import requests
from zhipuai import ZhipuAI

# zhupu api e58c6e65277b1b16dacac5c17fd3e2aa.Xo5pmhHSgXNFXFl4

domain = "comm.chatglm.cn"

url = f"https://{domain}/law_api/get_company_register"


headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer 1D1B44F1CCB5232426CA888EF0851AE0CFED6238191D8DD8'
}

data = {
    "company_name": "广州发展集团股份有限公司"
}

rsp = requests.post(url, json=data, headers=headers)
print(rsp.json())



client = ZhipuAI(api_key="e58c6e65277b1b16dacac5c17fd3e2aa.Xo5pmhHSgXNFXFl4") # 请填写您自己的APIKey

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_company_info",
            "description": "根据提供的公司名称，查询该公司的基本信息。包括公司简称、英文名称、关联证券、公司代码、曾用简称、所属市场、所属行业、上市日期、法人代表、总经理、董秘、邮政编码、注册地址、办公地址、联系电话、传真、官方网址、电子邮箱、入选指数、主营业务、经营范围、机构简介、每股面值、首发价格、首发募资净额、首发主承销商。",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "type": "string",
                        "description": "公司名称",
                    }
                },
                "required": ["company_name"],
            },
        }
    }
]
messages = [
    {
        "role": "user",
        "content": "我想要联系广州发展集团股份有限公司公司的法人代表，请问他的名字是什么？"
    }
]
response = client.chat.completions.create(
    model="glm-4", # 填写需要调用的模型名称
    messages=messages,
    tools=tools,
    tool_choice="auto",
)
print(response.choices[0].message)
print(f'response:{response}')

import json


# function = response.choices[0].message.tool_calls.function
# func_args = function.arguments
# func_name = function.name

function = response.choices[0].message.tool_calls[0].function
func_args = function.arguments
func_name = function.name
print(function)

url = f"https://{domain}/law_api/{func_name}"

print(url)

rsp = requests.post(url, json=json.loads(func_args), headers=headers)
print(rsp.json())