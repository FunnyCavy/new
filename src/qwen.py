import json

from openai import OpenAI

import env

sys_prompt = """
任务指令：处理用户上传的销项备注数据，提取每条备注中的区域信息与销项序号。根据区域信息匹配对应的销项表文件名，输出为JSON格式数组。若无法确定或未查找到对应文件，则该文件名输出为null。

输入格式：用户将上传一系列销项备注（每条备注包含明确的区域信息及销项序号），并附上拥有的销项表文件名。

处理步骤：
1. 分析每条销项备注，精确识别并提取销项序号（纯数字）及区域信息。
2. 根据提取的区域信息，查找匹配的销项表文件名（例如：xxx.xlsx, 注意实际文件名与区域的映射关系需根据实际情况确定）。
3. 组织输出数据，对于每条备注创建一个JSON对象，键值对分别为"file"（对应文件名）和"num"（销项序号）。如未找到匹配文件，"file"的值应设为null。

输出格式示例：
```json
[
  {"file": "区域A.xlsx", "num": 101},
  {"file": "区域B.xlsx", "num": 201},
  {"file": null, "num": 103}
]
```
注意：确保输出严格遵循上述JSON格式要求，不包含多余信息或格式错误。
"""


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
