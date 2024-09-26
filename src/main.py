import json
import re
from datetime import datetime
from pprint import pprint

import requests
from curlconverter import CurlConverter

import env
from src import excel_operator
from src import qwen

date_format = "%Y.%m.%d %H:%M"
need_format = "%m%d"

all_excel_files = excel_operator.read_all_excel_files(env.excel_folder_path)

pattern = r'```json(.*?)```'


def main():
    print("发送请求...")
    curl_converter = CurlConverter(env.http_request_template)
    curl_data = curl_converter.convert()

    request_url = curl_data['url']
    request_headers = {key.split(": ")[0]: key.split(": ")[1] for key, value in curl_data['headers'].items()}
    request_data = json.loads(curl_data['data'])

    response = requests.post(request_url, headers=request_headers, json=request_data)
    response_data = response.json()
    print("响应数据:\n" + str(response_data))

    # 解析原始数据
    print("解析原始数据...")
    all_photos_origin_data = []
    all_photos = response_data["data"]["photo"]
    for photo in all_photos:
        photo_pic_url = photo["media"]["picUrl"]
        photo_content_list = eval(photo["media"]["content"])

        photo_content_dict = {}
        for k, v in photo_content_list:
            photo_content_dict[k] = v

        photo_updater = photo_content_dict["上传人"]
        photo_date_origin = photo_content_dict["日期"]
        photo_date = datetime.strptime(photo_date_origin, date_format).strftime("%m%d")
        photo_remark = photo_content_dict["备注"]

        all_photos_origin_data.append({
            "url": photo_pic_url,
            "updater": photo_updater,
            "date_origin": photo_date_origin,
            "date": photo_date,
            "remark": photo_remark,
        })

    # AI 解析备注
    all_photos_origin_remarks = [photo["remark"] for photo in all_photos_origin_data]
    message = f"所有销项备注：\n" \
              f"{'\n'.join(all_photos_origin_remarks)}" \
              f"\n\n拥有的销项表文件：\n" \
              f"{'\n'.join(all_excel_files.keys())}"
    print("AI 调用解析备注:\n" + message)
    photo_remark_reply_json = qwen.get_response(message)
    print("AI 回复:\n" + photo_remark_reply_json)

    match = re.search(pattern, photo_remark_reply_json, re.S)
    json_str = match.group(1).strip()
    photo_remark_infos = json.loads(json_str)
    for i, photo_remark_info in enumerate(photo_remark_infos):
        photo_num = photo_remark_info["num"]
        photo_file_ = photo_remark_info["file"]
        photo_file = None
        if photo_file_ in all_excel_files:
            photo_file = all_excel_files[photo_file_]

        data = all_photos_origin_data[i]
        data["ai_reply"] = photo_remark_info
        data["excel_file"] = photo_file
        data["num"] = photo_num

    pprint(all_photos_origin_data)


if __name__ == "__main__":
    main()
