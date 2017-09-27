# 변수 이름은 문자, 숫자, _ 로 구성해야 한다.
# 처음실행은 ctr+shift + f10
# 같은 파일이면 shift + f10
import keyword
friend = 1
a = 10
my_name = '김규리'
_your_name = '둘리'
member1 = '마이콜'

# 에러
# $friend = 2
# a! = 1
# 1abc =10

# 에러: 예약어는 사용할 수 없다.
# def = 10

print(keyword.kwlist)

# 한글이름 의 변수도 가능하다
가격1 = 2000
print(가격1 - 200)
