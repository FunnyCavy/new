import json

from openai import OpenAI

import env
from src.excel_operator import read_all_excel_files

sys_prompt = """
用户将传入一句话，包含区域信息以及销项的序号。

请你根据区域信息找出关联的唯一 Excel 文件，并以 JSON 格式输出该 Excel 文件名、序号。
输出格式：{"file": "XXXX.xlsx", "num": 100}

可能关联的 Excel 文件名如下：
""" + "\n".join(read_all_excel_files(env.excel_folder_path).keys())


def get_response(content):
    client = OpenAI(
        api_key=env.ai_api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen-turbo",
        messages=[
            {'role': 'system', 'content': sys_prompt},
            {'role': 'user', 'content': content}
        ]
    )
    response_json = completion.model_dump_json()
    response_dict = json.loads(response_json)
    return response_dict['choices'][0]['message']['content']


if __name__ == '__main__':
    reply_json = get_response('五标段58–14B土建：（23）已销项')
    print(json.loads(reply_json))
