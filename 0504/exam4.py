# 전역 변수
student_score = 0

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

# 예제 실행
update_score(85)  # 점수를 85로 업데이트
grade_student()   # 업데이트된 점수를 바탕으로 학생의 등급 평가 및 출력
reset_score()     # 점수 초기화
