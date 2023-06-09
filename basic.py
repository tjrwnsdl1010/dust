# 1 대소문자로 데이터를 구분 apple != Apple
# 2 명령어의 띄어쓰기 주의
# 3 message / massage 오타 조심


# 변수 variable
dust = 10
dust = '10'
greeting = 'hello'

# 1
status = True
# 0
status = False

print(dust, greeting, status)

# List, 배열
dust_list = [10, 20, 20, 15, 100, 150]
print(dust_list[1])

# Dictionary
dust_dict = {
    '서울': 100,
    '대전': 50,
    '부산': 10,
}

print(dust_dict['서울'])

# 조건문
age = 10

if age > 20: 
    print('성인입니다.')
elif age > 8:
    print("청소년입니다.")
else:
    print('어린이입니다.')

# 반복문
menus = ['짜장면', '국밥', '김밥', '라면', '피자']

n = 0
while n < 4:
    print(menus[n])
    n += 1

print('----------------------------------')

for menu in menus:
    print(menu)