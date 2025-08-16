# cursor_test.py - Cursor에서 만든 첫 번째 파일

import datetime

def cursor_hello():
    """Cursor에서 인사하는 함수"""
    now = datetime.datetime.now()
    print(f"🎉 안녕하세요! Cursor에서 작성했습니다!")
    print(f"📅 작성 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"💻 에디터: Cursor (VS Code보다 좋아요!)")
    
def project_info():
    """프로젝트 정보"""
    print("\n📋 프로젝트 정보:")
    print("- 목표: FastAPI 3ds Max 라이센스 시스템")
    print("- 현재: Cursor와 GitHub 연동 학습")
    print("- 다음: 실제 FastAPI 서버 개발")
    print("- 도구: Cursor + Git + GitHub")

if __name__ == "__main__":
    cursor_hello()
    project_info()
    
    print("\n🚀 Cursor로 개발하니까 정말 편하네요!")
    print("이제 GitHub에 자동으로 올려봅시다!")