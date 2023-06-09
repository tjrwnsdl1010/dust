num_list = [1,2,3,4,5] # 배열 생성

max_num = max(num_list) # max() 배열 요소 중 제일 높은값을 반환함

print(max_num)


#-------------------------------------------------------------------------------------
import random

random_number = random.randint(1, 46) # random.randint( , )는 인자로 범위를 정해 무작위 수를 반환함

print(random_number)
#-------------------------------------------------------------------------------------

#pip install requests 외부모듈(라이브러리, 패키지) 먼저 설치
import requests
#URL을 첨부하여 요청한다


#-------------------------------------------------------------------------------------
menus = ['김밥', '라면', '만두']

menu = random.choice(menus) # .choice는 배열 요소들 중 무작위로 값을 반환한다.
print(menu)
#-------------------------------------------------------------------------------------
numbers = range(1, 46) #range( , ) 는 범위를 두 인자로 정하고 그 범위에 연속된 숫자를 생성
luckyList=random.sample(numbers, 6)
print(luckyList)

num = 0
while num < 5:
    luckyList=random.sample(numbers, 6)
    print(luckyList)
    num += 1

repeat = range(1, 6)
for num in repeat:
    luckyList=random.sample(numbers, 6)
print(luckyList)
#-------------------------------------------------------------------------------------

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1070'

res = requests.get(URL)

data = res.json()
drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

luckyNumber = random.sample(range(1, 46), 6)
print(lotto_number,', ', luckyNumber)

result = set(lotto_number) & set(luckyNumber)

print(result)