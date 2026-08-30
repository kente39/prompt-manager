# 나만의 프롬프트 관리 프로그램 (필수 완성 버전)
# 데이터는 메모리에만 저장되며, 프로그램을 종료하면 초기화됩니다.
# (JSON 파일 저장 등은 보너스이므로 이 버전에는 포함하지 않았습니다.)

# ---------- 기본 데이터 ----------
categories = ["소설", "에세이", "자기계발", "SF", "만화", "미스터리"]

prompts = [
    {"title": "에세이 초안", "content": "다음 주제로 개인적인 경험과 생각을 담은 에세이 초안을 써줘: ",
     "category": "에세이", "favorite": False},
    {"title": "네컷 만화 구성", "content": "다음 이야기를 기승전결이 있는 네컷 만화 형식으로 구성해줘: ",
     "category": "만화", "favorite": True},
    {"title": "자기계발 코치", "content": "너는 자기계발 코치야. 목표를 이룰 수 있게 실천 가능한 단계별 계획을 제안해줘.",
     "category": "자기계발", "favorite": False},
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
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


# ---------- 기능 함수 ----------
def add_prompt():                    # 역할: 입력을 받아 새 프롬프트를 리스트에 추가
    title = input_non_empty("제목: ")
    content = input_non_empty("내용: ")

    print("카테고리를 선택하세요:")
    for i, name in enumerate(categories, 1):
        print(f"  {i}. {name}")
    idx = input_number("번호 선택(직접 입력은 0): ", 0, len(categories))
    if idx == 0:
        category = input_non_empty("카테고리 직접 입력: ")
    else:
        category = categories[idx - 1]

    prompts.append({"title": title, "content": content,
                    "category": category, "favorite": False})
    print(f"'{title}' 추가 완료!")


def show_list():                     # 역할: 저장된 프롬프트를 번호와 함께 전부 출력
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, 1):
        star = "⭐" if p["favorite"] else "-"
        print(f"{i}. [{p['category']}] {p['title']} {star}")


def show_by_category():              # 역할: 고른 카테고리에 해당하는 프롬프트만 출력
    print("카테고리를 선택하세요:")
    for i, name in enumerate(categories, 1):
        print(f"  {i}. {name}")
    idx = input_number("번호 선택: ", 1, len(categories))
    target = categories[idx - 1]

    found = False
    for i, p in enumerate(prompts, 1):
        if p["category"] == target:
            print(f"{i}. {p['title']}")
            found = True
    if not found:
        print("해당 카테고리에 프롬프트가 없습니다.")


def search_prompt():                 # 역할: 키워드가 제목/내용에 든 프롬프트를 찾아 출력
    keyword = input_non_empty("검색어: ")
    found = False
    for i, p in enumerate(prompts, 1):
        if keyword in p["title"] or keyword in p["content"]:
            print(f"{i}. [{p['category']}] {p['title']}")
            found = True
    if not found:
        print("검색 결과가 없습니다.")


def show_detail():                   # 역할: 번호로 고른 프롬프트 1개의 전체 내용을 출력
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return
    show_list()
    idx = input_number("상세 볼 번호: ", 1, len(prompts))
    p = prompts[idx - 1]             # 사람 번호(1~) → 리스트 자리(0~)
    star = "⭐" if p["favorite"] else "-"
    print("-" * 30)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}  즐겨찾기: {star}")
    print(f"내용: {p['content']}")
    print("-" * 30)


def toggle_favorite():               # 역할: 번호로 고른 프롬프트의 즐겨찾기를 켜고/끔
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return
    show_list()
    idx = input_number("즐겨찾기 토글할 번호: ", 1, len(prompts))
    p = prompts[idx - 1]
    p["favorite"] = not p["favorite"]            # True↔False 뒤집기
    state = "추가" if p["favorite"] else "해제"
    print(f"'{p['title']}' 즐겨찾기 {state}!")


def show_favorites():                # 역할: 즐겨찾기(⭐)된 것만 모아서 출력
    favs = [p for p in prompts if p["favorite"]]
    if len(favs) == 0:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return
    for i, p in enumerate(favs, 1):
        print(f"{i}. [{p['category']}] {p['title']} ⭐")


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
            print("잘못된 번호입니다.")


# ---------- 실행 진입점 ----------
if __name__ == "__main__":
    main()
