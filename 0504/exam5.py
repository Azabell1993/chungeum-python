# 전역 변수
student_score = 0
input_count = 0  # 입력 횟수를 측정하는 변수

def update_score(score):
    global student_score
    student_score = score
    print(f"점수가 {student_score}로 업데이트 되었습니다.")

def grade_student():
    # 점수에 따라 학생의 성적을 등급으로 분류하고 적절한 메시지를 출력합니다.
    if student_score >= 90:
        print("등급: A - 탁월한 성적입니다!")
    elif student_score >= 80:
        print("등급: B - 잘했습니다!")
    elif student_score >= 70:
        print("등급: C - 만족스럽지만 개선이 필요합니다.")
    elif student_score >= 60:
        print("등급: D - 개선이 필요합니다.")
    else:
        print("등급: F - 불량입니다, 지도교수와 상담하세요.")

def reset_score():
    global student_score
    student_score = 0
    print("점수가 초기화되었습니다.")

# 점수 입력과 등급 평가를 반복합니다.
while True:
    score_input = input("학생의 점수를 입력하세요 (종료하려면 'exit' 입력): ")
    if score_input.lower() == 'exit':
        break
    if score_input.isdigit():
        update_score(int(score_input))
        grade_student()
        input_count += 1
    else:
        print("유효하지 않은 입력입니다. 숫자를 입력해 주세요.")

print(f"총 입력 횟수: {input_count}")
reset_score()  # 모든 입력 후 점수 초기화