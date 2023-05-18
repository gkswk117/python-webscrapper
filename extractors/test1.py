# 0.0-4.4
def test1():
  var_1 = 123
  var_2 = 23
  print(var_1+var_2)
  var_1 = "123"
  var_2 = "23"
  print("my name is", var_1+var_2)
  var_1 = True
  var_2 = False
  if var_1:
    print("rlahfl")
    print(type(var_1))
  
  ###function
  def first_function(a,b):
    print("Hello world.", a, b)
    
    print("----------------")
    # 파이썬에서는 중괄호가 없다. 그래서 탭의 위치(들여쓰기, indentation)가 정말 중요하다.
    # 같은 깊이를 가지는 명령문들은 하나의 묶음, 즉, 코드 블록(code block)으로 간주한다.
    # a, b는 parameter, "기모찌", "데스네"는 argument
  first_function("기모찌", "데스네.")
  first_function(b="데스네.", a="기모찌")
  # 첫번째 방법은 순서, 위치가 중요함.
  # 두번째 방법은 argument의 이름을 적어 줬기 때문에 순서, 위치 상관없음. 자바스크립트에서는 보지 못했던 방식.
  
  ###default parameters
  def default_parameters_function(par="홍길동"):
    print("hello", par)
  
  default_parameters_function("gkswk")
  default_parameters_function()
  
  ###return
  def first_function(a,b):
    return a+b
  
  print(first_function(1,2))
  # 파이썬에서는 같은 이름으로 함수를 두 번 정의해도 에러를 일으키지 않는다.
  
  def pick_fruit(fruit):
    return f"cup, {fruit}"
  # 파이썬에서 문자열에 변수를 집어넣는 방법. f => format 약자.
  def add_ice(pre):
    return f"{pre}, ice"
  
  def add_sugar(pre):
    return f"{pre}, sugar"
  
  print(add_sugar(add_ice(pick_fruit("banana"))))
  
  ###조건문 conditional
  
  number = 1
  if number>20:
    print("high score")
  elif number<=20 and number>=10:
    print("middle score")
  else:
    print("low score")
  
  ###input
  #콘솔창에서 값을 입력받고, 입력받은 값을 리턴하는 함수
  age = 3 #input("how old are you?")
  print("I'm", age)
  print(type(age))
  print(type(int(age)))
  #문자열->숫자로 바꾸고 싶으면 int 함수를 이용한다.
  print(type(123))
  print(type(str(123)))
  #숫자->문자열로 바꾸고 싶으면 str 함수를 이용한다.
  
  ###python standard library, randint
  from random import randint
  #random이라는 모듈에서 randint라는 함수를 가져오시오.
  computer_choice = randint(1,50)
  print(computer_choice)
  
  ###Python Casino
  a = True
  count = 0
  while a:
    if count ==10:
      count = count+1
      break
    user_choice = int(input("1~50 사이 숫자 중 하나를 고르시오."))
    if computer_choice == user_choice:
      print("Correct!")
      count= count+1
      a=False
    elif computer_choice > user_choice:
      print("Up!")
      count= count+1
    elif computer_choice < user_choice:
      print("Down!")
      count= count+1
  print("your score is ", (11-count))
  #1번째 맞추면 10점, 2번째 맞추면 9점 ... 10번째 맞추면 1점, 10번째 틀리면 0점이고 게임 종료.
  
  ###Python Practice 1
  a=True
  while a:
    a = input("원하는 값을 입력하시오")
    print("입력한 값은", a)
    a= bool(a)
    print(type(a))
    if a:
      print("a는 True이다.")
      print("종료하고 싶으면 빈 문자열을 입력하시오.")
    else:
      print("a는 False이다.")
  #여기서는 False를 입력해서 boolean으로 형변환을 해도 True이다.
  #string을 boolean으로 변환할 때 빈 문자열은 False, 그 외에는 모두 True이기 때문.
  #따라서 아래처럼 작성해야 한다.
  
  ###Python Practice 2
  while a!="False":
    a = input("이제 \"False\"를 입력하면 종료.")
    print("기모찌 is ", a)
    print(type(a))
  
  
  ### method, list, tuple
  name= "nico"
  print(name.capitalize())
  list = ["a","b","c","d"]
  print(list.append("e"))
  print(list[1],list[-1])
  tuple = ("a","b","c","d")
  print(tuple[1])
  # tuple = immutable list
  
  
    
  keey="eee"
  dict= {
    "name":"nico",
    "age":12,
    "alive":True,
    "fav_food":["milk","apple"],
    "friend":{
      "name":"lynn",
      "fav_food":["melon","bulgogi"],
    },
    # def dict_function():
    #   print("dkssud")
  }
  # javascript에서는 객체 안에 함수를 넣어서 내가 method를 만들 수 있었는데, python은 dictionary안에 함수를 넣을 수 없는 듯. 그냥 python에서 만들어 놓은 method만 쓸 수 있는듯.
  print(dict)
  print(dict.get("name"))
  print(dict["name"])
  # javascript에서는 dict.eee라고 하면 되는데 파이썬은 위의 두가지 방법이 있음.
  
  dict["level"]=273
  dict["fav_food"].append("orange")
  print(dict)
  print(dict["friend"]["fav_food"])
  print(dict["friend"]["fav_food"][0])
  
  