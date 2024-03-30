import requests
import json

session = requests.Session()

cookies = ""

session.cookies['JSESSIONID'] = cookies

# cookies = {
#     "gznotes-visited":
#     "true",
#     "Hm_lvt_f05f30f702742b6da7e05b7a691087cc":
#     "1711205442,1711207194,1711214860,1711267237",
#     "Hm_lpvt_f05f30f702742b6da7e05b7a691087cc":
#     "1711286529",
#     "JSESSIONID":
#     "ygFwuzS1Xp2Id9GWPj0pNS917hzDpTWidqzoAOBGfs8IH1E32XrX!-1475155454"
# }

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "Cookie": cookies,
    "Referer": "http://zxszhsz.tj.edu.cn/zhszpjcz/web/jbqk/xsXqDack.htm?stuFlag=1",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

data = {"method": "queryXsXqda", "pageSize": "3"}

url = "http://zxszhsz.tj.edu.cn/zhszpjcz/web/jbqk/xsXqDack.do"
url1 = "http://zxszhsz.tj.edu.cn/zhszpjcz/web/common/header.do"

response = session.post(url=url, data=data, headers=headers)
# if response.status_code == 200:
#     print(response.text)
#     # data = json.loads(response.text)
#     # for i in data:
#     # print(i)
# else:
#     print("请求失败", response.status_code)
print(response.text)
print(response.status_code)
print(response.url)
# print(response.content.decode("utf-8"))
