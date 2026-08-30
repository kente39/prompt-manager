# 나만의 책 관리 프로그램 (필수 완성 버전)
# 데이터는 메모리에만 저장되며, 프로그램을 종료하면 초기화됩니다.
# (JSON 파일 저장 등은 보너스이므로 이 버전에는 포함하지 않았습니다.)

# ---------- 기본 데이터 ----------
genres = ["소설", "에세이", "자기계발", "SF", "만화", "미스터리"]

books = [
    {"title": "어린 왕자", "author": "생텍쥐페리", "genre": "소설", "owned": True},
    {"title": "프로젝트 헤일메리", "author": "앤디 위어", "genre": "SF", "owned": False},
    {"title": "모방범", "author": "미야베 미유키", "genre": "미스터리", "owned": True},
]


# ---------- 입력 검증 유틸 ----------
def input_non_empty(message):        # 역할: 빈 값이면 다시 물어보고, 채워지면 그 값을 반환
    while True:
        value = input(message).strip()
        if value:
            return value
        print("빈 값은 입력할 수 없습니다. 다시 입력해주세요.")


def input_number(message, min_value, max_value):   # 역할: 숫자 + 범위까지 확인한 안전한 번호만 반환
    while True:
        value = input(message).strip()
        if not value.isdigit():
            print("숫자를 입력해주세요.")
            continue
        number = int(value)
        if number < min_value or number > max_value:
            print("범위를 벗어난 번호입니다.")
            continue
        return number


# ---------- 화면 출력 ----------
def show_menu():                     # 역할: 고를 수 있는 메뉴를 화면에 출력 (문구는 자유)
    print("\n=== 나만의 책 관리 ===")
    print("1. 책 추가")
    print("2. 책 목록")
    print("3. 장르별 조회")
    print("4. 검색")
    print("5. 상세 보기")
    print("6. 보유 상태 관리")
    print("7. 보유 목록")
    print("0. 종료")


# ---------- 기능 함수 ----------
def add_prompt():                    # 역할: 입력을 받아 새 책을 리스트에 추가
    title = input_non_empty("제목: ")
    author = input_non_empty("저자: ")

    print("장르를 선택하세요:")
    for i, name in enumerate(genres, 1):
        print(f"  {i}. {name}")
    idx = input_number("번호 선택(직접 입력은 0): ", 0, len(genres))
    if idx == 0:
        genre = input_non_empty("장르 직접 입력: ")
    else:
        genre = genres[idx - 1]

    books.append({"title": title, "author": author,
                  "genre": genre, "owned": False})
    print(f"'{title}' 추가 완료!")


def show_list():                     # 역할: 저장된 책을 번호와 함께 전부 출력
    if len(books) == 0:
        print("등록된 책이 없습니다.")
        return
    for i, b in enumerate(books, 1):
        mark = "📖 보유" if b["owned"] else "미보유"
        print(f"{i}. [{b['genre']}] {b['title']} - {b['author']} ({mark})")


def show_by_category():              # 역할: 고른 장르에 해당하는 책만 출력
    print("장르를 선택하세요:")
    for i, name in enumerate(genres, 1):
        print(f"  {i}. {name}")
    idx = input_number("번호 선택: ", 1, len(genres))
    target = genres[idx - 1]

    found = False
    for i, b in enumerate(books, 1):
        if b["genre"] == target:
            print(f"{i}. {b['title']} - {b['author']}")
            found = True
    if not found:
        print("해당 장르에 책이 없습니다.")


def search_prompt():                 # 역할: 키워드가 제목/저자에 든 책을 찾아 출력
    keyword = input_non_empty("검색어: ").lower()
    found = False
    for i, b in enumerate(books, 1):
        if keyword in b["title"].lower() or keyword in b["author"].lower():
            print(f"{i}. [{b['genre']}] {b['title']} - {b['author']}")
            found = True
    if not found:
        print("검색 결과가 없습니다.")


def show_detail():                   # 역할: 번호로 고른 책 1개의 전체 내용을 출력
    if len(books) == 0:
        print("등록된 책이 없습니다.")
        return
    show_list()
    idx = input_number("상세 볼 번호: ", 1, len(books))
    b = books[idx - 1]               # 사람 번호(1~) → 리스트 자리(0~)
    mark = "보유" if b["owned"] else "미보유"
    print("-" * 30)
    print(f"제목: {b['title']}")
    print(f"저자: {b['author']}")
    print(f"장르: {b['genre']}  보유: {mark}")
    print("-" * 30)


def toggle_favorite():               # 역할: 번호로 고른 책의 보유 상태를 켜고/끔
    if len(books) == 0:
        print("등록된 책이 없습니다.")
        return
    show_list()
    idx = input_number("보유 상태를 바꿀 번호: ", 1, len(books))
    b = books[idx - 1]
    b["owned"] = not b["owned"]                  # True↔False 뒤집기
    state = "보유" if b["owned"] else "미보유"
    print(f"'{b['title']}' → {state}(으)로 변경!")


def show_favorites():                # 역할: 보유(📖)한 것만 모아서 출력
    owned_books = [b for b in books if b["owned"]]
    if len(owned_books) == 0:
        print("보유한 책이 없습니다.")
        return
    for i, b in enumerate(owned_books, 1):
        print(f"{i}. [{b['genre']}] {b['title']} - {b['author']} 📖")


# ---------- 실행 흐름 ----------
def main():                          # 역할: 메뉴를 반복 출력하며 선택에 따라 기능 실행
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 0부터 7 사이의 번호를 입력해주세요.")


# ---------- 실행 진입점 ----------
if __name__ == "__main__":
    main()
