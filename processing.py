# 입력된 사이트 주소(URL)로부터 아래 규칙에 따라 비밀번호를 생성하는 프로그램을 작성하시오.

# - 예시 입력: `http://naver.com`
# - 규칙 1: `http://` 부분은 제외한다. ⇒ `naver.com`
# - 규칙 2: 처음 만나는 점(`.`) 이후 부분은 제외한다. ⇒ `naver`
# - 규칙 3: 남은 글자를 이용해 **처음 3자리 + 글자 개수 + 글자 내 'e' 개수 + '!'** 로 비밀번호를 만든다.
# - 예시 출력: `nav51!`

# 내가 푼 문제
naver1 = "http://naver.com"
naver2 = naver1[7:]
naver3 = naver2[:5]
print(f"{naver3[:3]}{len(naver3)}{naver3.count("e")}!")
# 코드를 이런식으로 짤 경우 주소를 변경하였을때 조건 2가 만족하지 않음
# naver2 = naver[7:]처럼 고정 길이로 슬라이싱 하면 google, youtube처럼 길이가 다른 사이트에서 규칙 2가 어긋남

# 답
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1 replace : 문자열 일부를 찾아 변경 => naver.com
my_str = my_str[:my_str.index(".")] # 규칙 2 index : 입력한 값을 찾음 my_str[0:5] -> 0~5 직전까지 => naver
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))
