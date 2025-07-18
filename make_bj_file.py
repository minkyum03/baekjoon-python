import os
from datetime import datetime

# 문제 번호 입력
problem_number = input("문제 번호를 입력하세요: ").strip()

# 날짜 폴더 생성
today = datetime.now().strftime("%Y-%m-%d")
folder_path = os.path.join(os.getcwd(), today)
os.makedirs(folder_path, exist_ok=True)

# 파일 경로 생성
file_name = f"{problem_number}.py"
file_path = os.path.join(folder_path, file_name)

# 템플릿 내용
template = f"""# 백준 {problem_number}번

def main():
    pass

if __name__ == "__main__":
    main()
"""

# 파일 생성
with open(file_path, "w", encoding="utf-8") as f:
    f.write(template)

print(f"{file_path} 파일이 생성되었습니다.")

# ✅ VS Code에서 자동으로 열기 (Windows 기준)
os.system(f'code "{file_path}"')
