from requests import get
from bs4 import BeautifulSoup

def extract_jobs_from_wwr(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  print(base_url+"기모찌!!!"+keyword)
  response = get(base_url+keyword)
  print(type(response))
  if response.status_code!=200:
    print("서버랑 연결할 수 없습니다.")
  else:
    job_datas = []
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(type(soup))
    jobs = soup.find_all('section', class_="jobs")
    # print(jobs[0])
    # print(len(jobs))
    # print(type(jobs))
    for jobs_section in jobs:
      jobs_post = jobs_section.find_all('li', class_="feature")
      for post_li in jobs_post:
        # print(post_li)
        # print(len(post_li))
        # print(post_li.find_all(class_="title"))
        # print(type(post_li))
        # print(len(jobs_post))
  
        anchors= post_li.find_all('a')
        anchor=anchors[1]
        # print(anchor)
        print(anchor["href"])
        link = anchor["href"]
        company, time, region = anchor.find_all('span', class_="company")
        print(company.string)
        title = anchor.find('span', class_="title")
        print(title.string)
        job_datas.append(
        {
          "link":f"https://weworkremotely.com{link}",
          "company":company.string,
          "region":region.string,
          "title":title.string,
        })
        
        print("/////////li///////")
      print("mmmmmmmmmmmmmmmsectionmmmmmmmmmmmmmmmm")
    # 여기서 jobs, jobs_section, jobs_post, post는 단순히 List가 아니라 14줄의 soup과 같이 beautifulsoup의 instance이다.
    # 타입을 출력해보면 클래스 bs4.element.tag라고 나온다.
    # instance의 안에 있는 attribute에 접근하는 방법 = > .(dot)
    
    # instance vs dictionary
    # instance는 attribute, dictionary는 key
    # instance는 ins.attr, dictionary는 dic["key"]로 접근한다.
      
  
    for each in job_datas:
      print(each)
    
    liiii = [1,2,3,4]
    print(liiii)
    print(type(liiii))
    first, second, third, forth = liiii
    print(second)
    
    diccc = {
      "name":"gkswk"
    }
    print(diccc)
    print(diccc["name"])
    print(type(diccc))

    return job_datas