#  외부라이브러리 사용

import requests as rq

response = rq.get("https://www.google.com")

print(response.status_code)
print(response.content) # 웹 브라우저 대신 http프로토콜  호출