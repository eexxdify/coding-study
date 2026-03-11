# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
from random import *
1st = [1,2,3,4,5]
print(1st)
shuffle(1st)
print(1st)
print(sample(1st, 1))


# 내 답안
from random import * # 틀린건 없지만 import random으로 더 간단히 사용가능.
first_place = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# range함수를 이용하면 다 적을 필요없이 range(1,21) 로 작성, 단 type이 range로 바뀌어 list에서 쓰고자 하는 함수를 사용불가.
# 이를 first_place = list(first_place)를 사용하면 type이 list로 바뀌면서 함수 사용가능.
shuffle(first_place)
print(" -- 당첨자 발표 -- 
치킨 당첨자 : ", first_place.pop())
print("커피 당첨자 : ", sample(first_place, 3), "
 -- 축하합니다 --")


# 답안
from random import * 
users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users)) # type range
users = list(users)
# print(type(users)) # type list

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")
