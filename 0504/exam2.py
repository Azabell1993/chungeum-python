def manage_pet_stats():
    # 지역 변수 초기화
    고양이_사료 = 120  # 고양이 사료 소비량 (그램)
    햄스터_물 = 300  # 햄스터 물 마심량 (밀리리터)
    파충류_온도 = 26  # 파충류 필요 온도 (도씨)
    새_비행시간 = 5  # 새의 비행 시간 (시간)

    # 전역 변수 초기화
    합계 = 고양이_사료 + 햄스터_물  # 고양이와 햄스터의 총 사료 및 물 소비량
    종합 = 파충류_온도 + 새_비행시간  # 파충류와 새의 관리 데이터 합

    # 결과 출력
    print(f"고양이와 햄스터의 총 사료 및 물 소비량: {합계} (그램 + 밀리리터)")
    print(f"파충류와 새의 관리 데이터 합: {종합} (도씨 + 시간)")

# 함수 실행
manage_pet_stats()