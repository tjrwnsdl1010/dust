num_list = [1,2,3,4,5]

max_num = max(num_list)

print(max_num)


########
import random

random_number = random.randint(1, 46)

print(random_number)

#######
#pip install requests 외부모듈(라이브러리, 패키지) 먼저 설치
import requests
#URL을 첨부하여 요청한다

#####

menus = ['김밥', '라면', '만두']

menu = random.choice(menus)
print(menu)

numbers = range(1, 46)
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