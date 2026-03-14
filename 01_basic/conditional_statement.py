# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [o] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

# 내 답안
from random import *
for customer in range(1, 51): # 승객은 인원은 있으나, 총 탑승 승객 수가 없음
  time_taken = randrange(5, 51)
  if time_kaken in randrange(5, 51): # randrange()는 난수를 다시 생성하는 함수, 조건 비교에 맞지않음. 
    print("[o] {0}번째 손님 (소요시간 : {1}분)".format(customer, time_taken))
  else:
    print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time_taken))


# 답안
from random import *
final_customer = 0 # 총 탑승 승객 수
for customer in range(1, 51): # 1~50 (승객)
  time_taken = randrange(5, 51) # 소요시간 5분 ~ 50분
  if 5 <= time_taken <= 15: # 소요시간 5분 ~ 15분
    print("[o] {0}번째 손님 (소요시간 : {1}분)".format(customer, time_taken))
    final_customer += 1
  else: # 매칭실패
    print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time_taken))
print("총 탑승 승객 : {}".format(final_customer))
