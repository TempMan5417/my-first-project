# hello.py - 내 첫 번째 Python 파일

def say_hello(name):
    """인사말을 출력하는 함수"""
    return f"안녕하세요, {name}님! GitHub에 오신 걸 환영합니다! 🎉"

def main():
    """메인 함수"""
    user_name = "개발자"
    message = say_hello(user_name)
    print(message)
    
    # 프로젝트 정보
    print("\n📋 프로젝트 정보:")
    print("- 목표: FastAPI 3ds Max 라이센스 시스템")
    print("- 현재 단계: GitHub 맛보기")
    print("- 상태: 학습 중 💪")

if __name__ == "__main__":
    main()
