import requests

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
domain = "comm.chatglm.cn"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 1D1B44F1CCB5232426CA888EF0851AE0CFED6238191D8DD8'
}

def func(api_id:int, messages:dict):

    url = f"https://{domain}/law_api/{apis[api_id]}"
    rsp = requests.post(url, json=messages, headers=headers)

    return rsp.json()


if __name__ == "__main__":
    url = f"https://{domain}/law_api/search_company_name_by_register"
    data = {
        "key": "统一社会信用代码",
        "value": "91440101231243173M"
    }

    rsp = requests.post(url, json=data, headers=headers)
    print(rsp.json())