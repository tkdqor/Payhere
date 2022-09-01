# Payhere

<br>

## ✅ 프로젝트 개요
- 페이히어 개발과제를 진행합니다. 
- 고객이 본인의 소비내역을 기록/관리할 수 있습니다.
- DRF를 바탕으로 API 서버를 구축하고 DRF simpleJWT로 토큰 인증을 구현했습니다.

<br>

## 🛠 사용 기술
- API 서버<br>
![python badge](https://img.shields.io/badge/Python-3.9-%233776AB?&logo=python&logoColor=white)
![django badge](https://img.shields.io/badge/Django-4.0.6-%23092E20?&logo=Django&logoColor=white)
![DRF badge](https://img.shields.io/badge/DRF-%23092E20?&logo=DRF&logoColor=white)
![DRFsimpleJWT badge](https://img.shields.io/badge/DRFsimpleJWT-%23092E20?&logo=DRF&logoColor=white)

- DB<br>
![Mysql badge](https://img.shields.io/badge/Mysql-%23092E20?&logo=Mysql&logoColor=white)

- ETC<br>
  <img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=Git&logoColor=white"/>
  
<br>

## :black_nib: 이슈 관리
<img width="1110" alt="image" src="https://user-images.githubusercontent.com/95380638/187826880-b582e49e-b581-4e7f-ab82-8376b14978aa.png">

**수행해야 할 개발 사항을 깃허브 이슈로 생성하고 칸반보드로 태스크 및 일정관리를 진행했습니다.** <br>

<br>

## ✨🍰✨ 코드 컨벤션

**Formatter**
- isort
- black

**Lint**
- flake8
<br>

**로컬에서 pre-commit 라이브러리를 사용해서 git commit 전에 3가지의 라이브러리를 한번에 실행하여 코드 컨벤션을 준수합니다. 만약 통과되지 않는다면 커밋이 불가능하게 설정합니다.**

<br>

## 🌟 API 명세서


<br>

## 📋 ERD


<br>

## ✔ 커밋 컨벤션
```terminal
# --- 제목(title) - 50자 이내로 ---
# <타입(type)> <제목(title)>
# 예시(ex) : Docs(Add) Commit docs Add

# --- 본문(content) - 72자마다 줄바꾸기  ---
# 예시(ex) :
# - Workflow
# 1. 커밋 메시지에 대한 문서 제작 추가.
# 2. commit message docs add.

# --- 꼬리말(footer) ---
# <타입(type)> <이슈 번호(issue number)>
# 예시(ex) : Fix #122

# --- COMMIT END ---
# <타입> 리스트
#   init    : 초기화
#   feat    : 기능추가
#   add     : 내용추가
#   update  : 기능 보완 (업그레이드)
#   fix     : 버그 수정
#   refactor: 리팩토링
#   style   : 스타일 (코드 형식, 세미콜론 추가: 비즈니스 로직에 변경 없음)
#   docs    : 문서 (문서 추가(Add), 수정, 삭제)
#   test    : 테스트 (테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없음)
#   chore   : 기타 변경사항 (빌드 스크립트 수정 등)
# ------------------
#     제목 첫 글자를 대문자로
#     제목은 명령문으로
#     제목 끝에 마침표(.) 금지
#     제목과 본문을 한 줄 띄워 분리하기
#     본문은 "어떻게" 보다 "무엇을", "왜"를 설명한다.
#     본문에 여러 줄의 메시지를 작성할 땐 "-" 혹은 "번호"로 구분
# ------------------
```

<br>

## 🧑‍💻 브랜치 전략
- main : 최종적으로 문제가 없고 완전히 개발된 기능을 포함하는 브랜치
- feature : issue에 부여한 기능을 개발하는 브랜치로 기능 개발이 완료되면 main 브랜치에 Merge 진행

<br>

## 📝 주석 처리
```python
# url : GET, POST api/v1/restaurants
class RestaurantAPIView(APIView):
    """
    Assignee : 상백

    permission = 작성자 본인만 가능
    Http method = GET, POST
    GET : 가계부 목록 조회
    POST : 가계부 생성
    """
    ...
```
- View 클래스 하단에 해당 코드에 대한 설명을 여러 줄 주석으로 기재
- 한 줄 주석으로 클래스 위에 URL 기재

<br>


