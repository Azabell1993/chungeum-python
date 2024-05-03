# 전역 변수
number = 5

def print_number():
    # 지역 변수
    local_number = 10
    print("지역 변수:", local_number)
    print("전역 변수:", number)

print_number()
# 함수 외부에서 지역 변수에 접근하려고 하면 에러 발생
print(local_number)  # 이 부분을 주석 처리 해제하면 에러 확인 가능
