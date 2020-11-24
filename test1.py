import requests

url = "https://www.youtube.com/?gl=TW&hl=zh-TW"

payload = {}
headers = {
  'Cookie': 'YSC=7b1NZQ8FSTU; GPS=1; VISITOR_INFO1_LIVE=gxlNMPVIW0A; s_gl=ca02b225c88e6fda0cbe664706f57e38cwIAAABUVw=='
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
