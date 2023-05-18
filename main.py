from requests import get
from bs4 import BeautifulSoup

# 5.10 Refactor
from extractors.wwr import extract_jobs_from_wwr
from extractors.test1 import test1
from extractors.test2 import test2

# test1()
# test2()
keyword = "python"
job_datas_wwr = extract_jobs_from_wwr(keyword)

file = open(f"{keyword}_hanwoong.csv", "w")
# open => python 기본 내장 함수


file.write("Link,Company,Region,Title\n")
for each in job_datas_wwr:
  file.write(f"{each['link']},{each['company']},{each['region']},{each['title']}\n")

# 쌍따옴표 안에 또 쌍따옴표는 넣을 수 없지만 그럴땐 그냥 따옴표를 쓰면 된다.
file.close()