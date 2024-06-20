import requests
from zhipuai import ZhipuAI

from utils.func import func

client = ZhipuAI(api_key="e58c6e65277b1b16dacac5c17fd3e2aa.Xo5pmhHSgXNFXFl4") # 请填写您自己的APIKey


apis = {
    0: "get_company_info",
    1: "search_company_name_by_info",
    2: "get_company_register",
    3: "search_company_name_by_register",
    4: "get_sub_company_info",
    5: "search_company_name_by_sub_info",
    6: "get_legal_document",
    7: "search_case_num_by_legal_document"
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_company_register",
            "description": "根据提供的公司名称，查询该公司对应的法人代表。",
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



import json

domain = "comm.chatglm.cn"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 1D1B44F1CCB5232426CA888EF0851AE0CFED6238191D8DD8'
}

# function = response.choices[0].message.tool_calls.function
# func_args = function.arguments
# func_name = function.name

function = response.choices[0].message.tool_calls[0].function
func_args = function.arguments
func_name = function.name

url = f"https://{domain}/law_api/{func_name}"

print(url, json.loads(func_args))
print(headers)
rsp = requests.post(url, json=json.loads(func_args), headers=headers)
print(rsp.json())