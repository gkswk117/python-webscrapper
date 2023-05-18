# 4.5-4.9

from requests import get
def test2():
  websites = [
    "google.com",
    "airbnb.com",
    "https://facebook.com",
    "naver.com",
  ]
  
  print(websites.index("naver.com"))
  
  for each in websites:
    if not each.startswith("https://"):
      websites[websites.index(each)]=f"https://{each}"
  
  # python standard library에 다양한 모듈이 있지만, 이것만으로는 부족하다.
  # 다른 개발자들이 각자의 필요에 의해 직접 만든 모듈들이 수천만 가지가 된다.
  # pypi.org에서 다른 개발자들이 만들어 놓은 모듈을 확인할 수 있다.
  # 그중 하나인 requests 모듈을 써볼 것.
  
  print(websites)
  response= get(websites[0])
  print(response.status_code)
  print(response)