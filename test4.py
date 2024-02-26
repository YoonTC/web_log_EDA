import urllib.request
import re

# URL 설정
url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html"

# URL에서 HTML 내용을 가져옴
with urllib.request.urlopen(url) as response:
    html_contents = response.read().decode("utf8")
print(html_contents)
# zip 파일 링크 찾기
url_list = re.findall(r"http[s]?://.*?\.zip", html_contents)

# 링크 출력
for url in url_list:
    print(url)