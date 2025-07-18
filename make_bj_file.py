import os
from datetime import datetime

# 오늘 날짜 구하기
today = datetime.today().strftime('%Y-%m-%d')

# 날짜 폴더가 없다면 만들기
if not os.path.exists(today):
    os.makedirs(today)

# 사용자 입력으로 문제 번호 받기
problem_number = input("문제 번호를 입력하세요 (예: 10813): ").strip()

# 파일 경로 만들기
file_path = os.path.join(today, f"{problem_number}.py")

# 파일이 이미 있으면 덮어쓰기 방지
if os.path.exists(file_path):
    print(f"⚠️ 이미 {file_path} 파일이 존재합니다!")
else:
    # 파일 생성 및 기본 템플릿 쓰기
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# 백준 {problem_number}번\n\n")
        f.write(f"# 입력 예시:\n# \n\n# 출력 예시:\n# \n\n")

    print(f"✅ {file_path} 파일이 생성되었습니다!")
