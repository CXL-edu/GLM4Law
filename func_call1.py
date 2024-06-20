import json
import requests
from zhipuai import ZhipuAI
from dotenv import dotenv_values

# zhupu api e58c6e65277b1b16dacac5c17fd3e2aa.Xo5pmhHSgXNFXFl4

domain = "comm.chatglm.cn"
config = dotenv_values(".env")
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {config["team_token"]}'
}

client = ZhipuAI(api_key=config["zhipu_api"]) # 请填写您自己的APIKey

question = '上市公司因涉嫌金融诈骗面临的法律风险有哪些？'


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_company_info",
            "description": "根据提供的'公司名称'，查询该公司的'基本信息'。包括公司简称、英文名称、关联证券、公司代码、曾用简称、所属市场、所属行业、上市日期、法人代表、总经理、董秘、邮政编码、注册地址、办公地址、联系电话、传真、官方网址、电子邮箱、入选指数、主营业务、经营范围、机构简介、每股面值、首发价格、首发募资净额、首发主承销商。",
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
    },
    {
        "type": "function",
        "function": {
            "name": "search_company_name_by_info",
            "description": "根据'公司基本信息某个字段'是'某个值'来查询具体的'公司名称'",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "公司基本信息的某个字段",
                    },
                    "value": {
                        "type": "string",
                        "description": "公司基本信息的某个字段的值",
                    }
                },
                "required": ["key", "value"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_company_register",
            "description": "根据提供的'公司名称'，查询该公司的'注册信息'。",
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
    },
    {
        "type": "function",
        "function": {
            "name": "search_company_name_by_register",
            "description": "根据'公司注册信息某个字段'是'某个值'来查询具体的'公司名称'",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "公司注册信息某个字段。包括公司名称、登记状态、统一社会信用代码、注册资本、成立日期、省份、城市、区县、注册号、组织机构代码、参保人数、企业类型、曾用名。",
                    },
                    "value": {
                        "type": "string",
                        "description": "公司注册信息某个字段的值",
                    }
                },
                "required": ["key", "value"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_sub_company_info",
            "description": "根据提供的'公司名称'，查询该公司的'子公司信息'。包括关联上市公司股票代码、关联上市公司股票简称、关联上市公司全称、上市公司关系、上市公司参股比例、上市公司投资金额、公司名称。",
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
    },
    {
        "type": "function",
        "function": {
            "name": "search_company_name_by_sub_info",
            "description": "根据'关联子公司信息某个字段'是'某个值'来查询具体的'公司名称'。",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "关联子公司信息某个字段。包括关联上市公司股票代码、关联上市公司股票简称、关联上市公司全称、上市公司关系、上市公司参股比例、上市公司投资金额、公司名称。",
                    },
                    "value": {
                        "type": "string",
                        "description": "关联子公司信息某个字段的值",
                    }
                },
                "required": ["key", "value"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_legal_document",
            "description": "根据提供的'案号'，查询'法律文书信息'。包括标题、案号、文书类型、原告、被告、原告律师、被告律师、案由、审理法条依据、涉案金额、判决结果、胜诉方、文件名。",
            "parameters": {
                "type": "object",
                "properties": {
                    "case_num": {
                        "type": "string",
                        "description": "案号",
                    }
                },
                "required": ["case_num"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_case_num_by_legal_document",
            "description": "根据'法律文书某个字段'是'某个值'来查询具体的'案号'。",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "法律文书某个字段。包括标题、案号、文书类型、原告、被告、原告律师、被告律师、案由、审理法条依据、涉案金额、判决结果、胜诉方、文件名。",
                    },
                    "value": {
                        "type": "string",
                        "description": "法律文书某个字段的值",
                    }
                },
                "required": ["key", "value"],
            },
        }
    },
]
# messages = [
#     {
#         "role": "user",
#         "content": f"下面问题应该需要调用哪些工具？{question}",
#     }
# ]
# response = client.chat.completions.create(
#     model="glm-4", # 填写需要调用的模型名称
#     messages=messages,
#     tools=tools,
#     tool_choice="auto",
#     # do_sample=False,  # temperature、top_p 将不生效
# )
messages = [
    {
        "role": "system",
        "content": "你是一个超级助手，请将下面的问题分解为更小的子问题。这些问题将帮助你更好地回答用户的问题。"
    },
    {
        "role": "user",
        "content": f"{question}",
    }
]
response = client.chat.completions.create(
    model="glm-4", # 填写需要调用的模型名称
    messages=messages,
    # tools=tools,
    # tool_choice="auto",
    do_sample=False,  # temperature、top_p 将不生效
)
print(response.choices[0].message)
# print(response.choices[0].message.tool_calls)

function = response.choices[0].message.tool_calls[0].function
func_args = function.arguments
func_name = function.name

url = f"https://{domain}/law_api/{func_name}"
rsp = requests.post(url, json=json.loads(func_args), headers=headers)
rsp = rsp.json()
print(url)
print(rsp)

text = ''
for key, value in rsp.items():
    text += f"'{key}'是{value}，"
text = text[:-1] + '。'


messages = [
    {
        "role": "user",
        "content": f"已知所需相关信息如下：{text}。{question}",
    }
]

import time
t0 = time.time()
response = client.chat.completions.create(
    model="glm-4", # 填写需要调用的模型名称
    messages=messages,
    do_sample=False,  # temperature、top_p 将不生效
)
print(time.time()-t0)
print(response.choices[0].message.content)






























