books = [
    {
        "title": "어린 왕자",
        "author": "생텍쥐페리",
        "genre": "소설",
        "owned": True,
    },
    {
        "title": "프로젝트 헤일메리",
        "author": "앤디 위어",
        "genre": "SF",
        "owned": False,
    },
    {
        "title": "모방범",
        "author": "미야베 미유키",
        "genre": "미스터리",
        "owned": True,
    }
]
genres = ["소설", "에세이", "자기계발", "SF", "만화", "미스터리"]

def show_menu():
    print("\n=== 프롬프트 관리자 ===")
    print("1. 새 프롬프트 추가   2. 전체 프롬프트 목록")
    print("3. 카테고리별 조회 4. 검색")
    print("5. 상세 보기      6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록  0. 종료")

def add_prompt():      pass
def show_list():       pass
def show_by_category(): pass
def search_prompt():   pass
def show_detail():     pass
def toggle_favorite(): pass
def show_favorites():  pass

def main():
    while True:
        show_menu()
        choice = input("선택: ")
        if choice == "1":   add_prompt()
        elif choice == "2": show_list()
        elif choice == "0":
            print("프로그램을 종료합니다."); break
        else:            print("잘못된 번호입니다.")

if __name__ == "__main__":
    main()