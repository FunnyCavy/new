# Excel 表格文件夹 绝对路径
excel_folder_path = r"C:\Project\mine\OneMoreThing\test_excel"

# Qwen ApiKey
ai_api_key = "sk-8dcae3ecf2c9493abaad1e57efa230f4"

# 导出照片 -> 查询 | HTTP 请求模板
http_request_template = """
curl 'https://admin.markiapp.com/api/v1/searchTeamMediaV2' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H 'communityid: undefined' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'cookie: hiido_ui=0.7956308323210224; osudb_lang=zh-cn; osudb_third=0743f4ec88f1702163bc79944666ded215d9bdc7cb294d28b1614ca75b80b6aa5493a35a91a3f6d9860f2b04f1fdd3a017e2e560a0d3469ea470b2ca5fa49cd8255adb477bcceda99ff2677b4d5652ffc0de8730cb8b3f0949f97552483ff88f1ed2bfeaa8496aad313b6132b36890ccc4ba3cdbff10f7d25f648f9efc7e21e6698e211ccb2ce133825ae08ab64b5309b5a6a4159a8de63e095935ca1af8c8846dc1ffe0f23329854f28fcc29585ced12d05365372050023c26e67085adc4ab3b35f149b7b1e7477454288258d526c07967124c9919635e79f9317fc8a6e562ab6895b29ee7a7526c2776e9b32fc0ff07b95cc48a4d1b6cffd7191d174cf67b3; osudb_uid=4805078914; osudb_appid=1435186595; osudb_oar=085d4a88c5c5d3bbf5f5ee3314efa5fae4339c5e0788b0930ab6e898b4942989920107191c6fd94771d31633d051f93511030a17a62c28ca512ade7076ddc2ddaeeb70dc93ba72a099096c5bee9dc458cd5745546b3816d98fcde0d26bedd858673ac0bf823a26f239cab7faeb5c744cc3249212ca1a92532bbd22941643718f925fa5ebf7c7e58ab7f69c02b06caa75baf6b060bc8db1fcd2198b2e12e09cc6114e9dc5c57b5dcbf1d7b6e46234e004cb19ee4ff395b8046a7dcd49028eec4c5b2aefbe831dbdcf9595c8884289f257124e7e44971a51fcaa9cc583df5bbd6879affccb2752cf750e2524205a43c281c32abe63c93e8a8a6ef424185abc1f3d; osudb_c=00804132107a0001700028c5e005322b0d390377ee105604fa4030573146be449bb088212d861d4f39d4249f002dabefc3c509f43997a55797a12a54d4581a08ac54d7332486d55639479c6ba4c176c8f9a89ec43f28ea0e949166506399e2c4cbb7a75dc68dc2b038a3dc26bf608376e19171eeedcf0a459636; osudb_sex=0; osudb_param=; osudb_ustate=1; osudb_nickname=%E4%BB%8A%E5%A4%A9%E7%9A%84%E5%8D%A2%E6%B5%AE%E5%AE%AB%E5%B0%B1%E9%80%9B%E5%88%B0%E8%BF%99%E9%87%8C; osudb_avatar=https://thirdwx.qlogo.cn/mmopen/vi_32/aEJxRz5usnwDufztcX3A2scoZ78zOibWQ9hX6pib2VLCjT8q4K3LNIVjJB1esFhiaOHJgxwUyXGBHdGeWJzA1zG4gq0ChJEeC757hAXYyJDLZc/132' \
  -H 'origin: https://admin.markiapp.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://admin.markiapp.com/export/exportPic' \
  -H 'sec-ch-ua: "Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0' \
  -H 'x-authtype: 1' \
  --data-raw '{"teamID":"46018411","type":1,"page":1,"pageSize":30,"timeStart":"2024-09-21 00:00:00","timeEnd":"2024-09-21 23:59:59","uids":"4803120742","markID":"","searchType":0,"tagList":[],"blockInfo":""}'
"""

# 成员 UID
members_uid_dict = {
    "马冬": 4804180368,
    "张磊": 4800779048,
    "王子文": 4802879872,
    "马亮": 4801943928,
    "刘萌": 4801738584,
    "刘泽": 4803155627,
    "芦开": 4803102429,
    "邓超": 4803120742,
    "贾": 4803577461,
    "王锋": 4805078844,
    "张太": 4804462486,
    "李志": 4803755933,
    "陈学亮": 4804160936,
    "赵硕": 4802590994,
    "肖朋雷": 4800728451,
    "李坤": 3312981457,
    "邢宇飞": 4801943942,
    "谭兴政": 4802104070,
    "李宁": 4800842773,
    "崔艳学": 4802055516,
    "王新超": 4803966303,
    "刘正": 4803112785,
    "车汶桐": 4801498488,
    "齐涛": 4802095641,
    "韩泽": 3312981473,
    "李春喜": 4804180472,
    "曹文": 4802590930,
    "刘瑞雪": 4801495841,
    "夏家琦": 4805078914,
    "林森": 4802707105,
    "王旭": 4804647153,
    "杨洋": 4803817470,
    "孙向": 4801985464,
    "夏楠": 4804371879,
    "张岩": 4804140053,
    "任伟": 3312964748,
    "李佳乐": 3312901456,
    "郭辰旭": 3313457556,
    "朱玉成": 4801944053,
    "由聪": 3315399762,
    "朱栓利": 4801242309,
    "肖金良": 4800606742,
    "薛亮": 4802104052,
}
