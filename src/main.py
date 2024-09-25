import json
from datetime import datetime

import requests
from curlconverter import CurlConverter

from env import http_request_template

test_json = r"""
{
    "code": 0,
    "msg": "",
    "admin": 1,
    "data": {
        "photo": [
            {
                "momId": "7417016092521767330",
                "mediaId": "7417016092521767330",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:50:30+08:00",
                "media": {
                    "id": "7417016092521767330",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_380_965.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（43）已销项\"],[\"日期\",\"2024.09.21 16:50\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417015989442548840",
                "mediaId": "7417015989442548840",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:50:06+08:00",
                "media": {
                    "id": "7417015989442548840",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_206_302.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（23）已销项\"],[\"日期\",\"2024.09.21 16:50\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417013902088430818",
                "mediaId": "7417013902088430818",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:42:00+08:00",
                "media": {
                    "id": "7417013902088430818",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_830_773.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（13）已销项\"],[\"日期\",\"2024.09.21 16:41\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417013781829348545",
                "mediaId": "7417013781829348545",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:41:32+08:00",
                "media": {
                    "id": "7417013781829348545",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_64_115.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（10）已销项\"],[\"日期\",\"2024.09.21 16:41\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417013537016208478",
                "mediaId": "7417013537016208478",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:40:35+08:00",
                "media": {
                    "id": "7417013537016208478",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_125_732.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（28）已销项\"],[\"日期\",\"2024.09.21 16:40\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417013442526927428",
                "mediaId": "7417013442526927428",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:40:13+08:00",
                "media": {
                    "id": "7417013442526927428",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_365_95.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（27）已销项\"],[\"日期\",\"2024.09.21 16:40\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417013214893662124",
                "mediaId": "7417013214893662124",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:39:20+08:00",
                "media": {
                    "id": "7417013214893662124",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_207_13.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（156）已销项\"],[\"日期\",\"2024.09.21 16:39\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417013068864770464",
                "mediaId": "7417013068864770464",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:38:46+08:00",
                "media": {
                    "id": "7417013068864770464",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_421_441.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（153）已销项\"],[\"日期\",\"2024.09.21 16:38\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417012793986861805",
                "mediaId": "7417012793986861805",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:37:42+08:00",
                "media": {
                    "id": "7417012793986861805",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_914_577.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（103）已销项\"],[\"日期\",\"2024.09.21 16:37\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417012209871305983",
                "mediaId": "7417012209871305983",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:35:26+08:00",
                "media": {
                    "id": "7417012209871305983",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_119_565.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（414）已销项\"],[\"日期\",\"2024.09.21 16:35\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417012042367582971",
                "mediaId": "7417012042367582971",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:34:47+08:00",
                "media": {
                    "id": "7417012042367582971",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_995_496.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（30）已销项\"],[\"日期\",\"2024.09.21 16:34\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417011256388562602",
                "mediaId": "7417011256388562602",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:31:44+08:00",
                "media": {
                    "id": "7417011256388562602",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_49_220.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（234）已销项\"],[\"日期\",\"2024.09.21 16:31\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417010672273003932",
                "mediaId": "7417010672273003932",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:29:28+08:00",
                "media": {
                    "id": "7417010672273003932",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_290_702.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（73）已销项\"],[\"日期\",\"2024.09.21 16:29\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417010397395097866",
                "mediaId": "7417010397395097866",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:28:24+08:00",
                "media": {
                    "id": "7417010397395097866",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_498_721.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（115）已销项\"],[\"日期\",\"2024.09.21 16:28\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417010070977581142",
                "mediaId": "7417010070977581142",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:27:08+08:00",
                "media": {
                    "id": "7417010070977581142",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_304_144.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（91）已销项\"],[\"日期\",\"2024.09.21 16:27\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417009516926793941",
                "mediaId": "7417009516926793941",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:24:59+08:00",
                "media": {
                    "id": "7417009516926793941",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_728_737.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（109）已销项\"],[\"日期\",\"2024.09.21 16:24\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417009272113656481",
                "mediaId": "7417009272113656481",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:24:02+08:00",
                "media": {
                    "id": "7417009272113656481",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_763_155.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（97）已销项\"],[\"日期\",\"2024.09.21 16:24\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417009138969671957",
                "mediaId": "7417009138969671957",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:23:31+08:00",
                "media": {
                    "id": "7417009138969671957",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_623_663.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（96）已销项\"],[\"日期\",\"2024.09.21 16:23\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417008614983658367",
                "mediaId": "7417008614983658367",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:21:29+08:00",
                "media": {
                    "id": "7417008614983658367",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_940_571.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（20）已销项\"],[\"日期\",\"2024.09.21 16:21\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417004925606722709",
                "mediaId": "7417004925606722709",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:07:10+08:00",
                "media": {
                    "id": "7417004925606722709",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_393_61.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（285）已销项\"],[\"日期\",\"2024.09.21 16:07\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417004178282407449",
                "mediaId": "7417004178282407449",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:04:16+08:00",
                "media": {
                    "id": "7417004178282407449",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_638_31.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（577）已销项\"],[\"日期\",\"2024.09.21 16:04\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417003684361164558",
                "mediaId": "7417003684361164558",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T16:02:19+08:00",
                "media": {
                    "id": "7417003684361164558",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_306_324.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（286）已销项\"],[\"日期\",\"2024.09.21 16:02\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417003053000969099",
                "mediaId": "7417003053000969099",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T15:59:54+08:00",
                "media": {
                    "id": "7417003053000969099",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_301_36.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B市政园林：（4898）已销项\"],[\"日期\",\"2024.09.21 15:59\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417001996439004356",
                "mediaId": "7417001996439004356",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T15:55:48+08:00",
                "media": {
                    "id": "7417001996439004356",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_369_910.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（4826）已销项\"],[\"日期\",\"2024.09.21 15:55\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417001622776846987",
                "mediaId": "7417001622776846987",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T15:54:21+08:00",
                "media": {
                    "id": "7417001622776846987",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_597_826.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（262）已销项\"],[\"日期\",\"2024.09.21 15:54\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·春澜荟中区"
            },
            {
                "momId": "7417000634934362002",
                "mediaId": "7417000634934362002",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T15:50:31+08:00",
                "media": {
                    "id": "7417000634934362002",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_695_352.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（343）已销项\"],[\"日期\",\"2024.09.21 15:50\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417000398711159141",
                "mediaId": "7417000398711159141",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T15:49:36+08:00",
                "media": {
                    "id": "7417000398711159141",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_166_991.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（378）已销项\"],[\"日期\",\"2024.09.21 15:49\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7417000244092335476",
                "mediaId": "7417000244092335476",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T15:49:00+08:00",
                "media": {
                    "id": "7417000244092335476",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_560_186.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（320）已销项\"],[\"日期\",\"2024.09.21 15:48\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7416999797415735830",
                "mediaId": "7416999797415735830",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T15:47:16+08:00",
                "media": {
                    "id": "7416999797415735830",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_105_153.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（300）已销项\"],[\"日期\",\"2024.09.21 15:47\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            },
            {
                "momId": "7416999629912007946",
                "mediaId": "7416999629912007946",
                "uid": 4803120742,
                "userName": "邓超",
                "userIcon": "https://biu-cn.dwstatic.com/default/squareicon.png",
                "teamid": 46018411,
                "posttime": "2024-09-21T15:46:37+08:00",
                "media": {
                    "id": "7416999629912007946",
                    "type": 1,
                    "picUrl": "https://mk-n.dwstatic.com/mkc/default/4803120742/20240921/_678_152.jpg",
                    "videoUrl": "",
                    "content": "[[\"备注\",\"五标段58–14B土建：（259）已销项\"],[\"日期\",\"2024.09.21 15:46\"],[\"标题\",\"请输入内容\"],[\"上传人\",\"邓超\"]]",
                    "src": 0,
                    "markiId": "team_1349958"
                },
                "locationName": "河北省雄安新区容城县大河镇·良利烟酒"
            }
        ],
        "total": 102,
        "totalType": 0,
        "blockInfo": "{\"mode\":\"direct\",\"dli\":{\"1\":{\"li\":7416999629912007946,\"lt\":1726904797},\"2\":{\"li\":7416920911750973399,\"lt\":1726886469},\"3\":{\"li\":7416899655957631533,\"lt\":1726881520}}}",
        "endPageNo": 4
    }
}
"""

date_format = "%Y.%m.%d %H:%M"
need_format = "%m%d"

def main():
    resp = json.loads(test_json)
    photos = resp["data"]["photo"]
    for photo in photos:
        photo_pic_url = photo["media"]["picUrl"]
        photo_content_list = eval(photo["media"]["content"])

        photo_content_dict = {}
        for k, v in photo_content_list:
            photo_content_dict[k] = v

        photo_date = photo_content_dict["日期"]
        photo_updater = photo_content_dict["上传人"]
        photo_remark = photo_content_dict["备注"]

        print(photo_pic_url)
        print(photo_updater)
        print(datetime.strptime(photo_date, date_format).strftime("%m%d"))
        print(photo_remark)
        print("")


if __name__ == "__main__":
    main()
    #
    # curl_converter = CurlConverter(http_request_template)
    # curl_data = curl_converter.convert()
    #
    # url = curl_data['url']
    # headers = {key.split(": ")[0]: key.split(": ")[1] for key, value in curl_data['headers'].items()}
    # data = json.loads(curl_data['data'])
    #
    # response = requests.post(url, headers=headers, json=data)
    # print(response.json())
