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
![Mysql badge](https://img.shields.io/badge/Mysql-5.7-%23092E20?&logo=Mysql&logoColor=white)

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
<img width="1141" alt="image" src="https://user-images.githubusercontent.com/95380638/187829237-00fe4516-b9db-4b30-828b-8747aaa2c68c.png">

- **/api/v1/token/refresh** : 해당 API로 access token 및 refresh token 재발급할 수 있게 설정. settings.py에서 SIMPLE_JWT의 설정 중, ROTATE_REFRESH_TOKENS이라는 항목을 True로 설정하여 재발급 시, access token만 갱신되는 것이 아니라 refresh token도 같이 갱신되도록 진행.
- **/api/v1/users/restaurants/trash** : 해당 API로 로그인된 유저가 삭제한 가계부를 확인할 수 있도록 진행. 일반적인 휴지통과 같이 유저 본인이 확인한다는 개념으로 accounts 앱 View에 구성. 특정 가계부의 삭제한 레코드 목록 확인 API도 같은 맥락으로 설정.
- **/api/v1/restaurants/<restaurant_id>** : 해당 API로 특정 가계부 삭제 및 복구를 진행. is_deleted 필드를 true로 설정하고 요청하면 삭제가 되고 false로 설정하면 복구가 진행되도록 설정. PATCH의 경우, 멱등성이 보장되는 경우도 있고 아닌 경우도 있기에 따로 2개의 API URL를 구성할 필요가 없다고 판단. 특정 가계부에 속하는 단일 레코드 삭제 및 복구 API도 같은 맥락으로 설정.


<details>
<summary>🚀 API 호출 테스트 결과</summary>
<div markdown="1">
<ul>
  <li>
    <p>회원가입</p>
    <img width="857" alt="image" src="https://user-images.githubusercontent.com/95380638/187829439-b68340fa-a860-4e47-ad51-365c778fec14.png">
  </li>
  <li>
    <p>로그인</p>
    <img width="858" alt="image" src="https://user-images.githubusercontent.com/95380638/187829492-7512db15-6284-4181-9e55-8779b8700d78.png">
  </li>
  <li>
    <p>access token 및 refresh token 재발급</p>
    <img width="834" alt="image" src="https://user-images.githubusercontent.com/95380638/187829569-20f9c454-c1a0-4d1d-83b5-0a78f29725d0.png">
  </li>
  <li>
    <p>삭제한 가계부 목록 확인</p>
    <img width="846" alt="image" src="https://user-images.githubusercontent.com/95380638/187829691-60f5361a-cccc-457d-8137-b300cf68a9e7.png">
  </li>
  <li>
    <p>특정 가계부의 삭제한 레코드 목록 확인</p>
    <img width="866" alt="image" src="https://user-images.githubusercontent.com/95380638/187829806-7461cec0-ac0f-48b1-8cb0-eab45184cd5a.png">
  </li>
  <li>
    <p>가계부 생성</p>
    <img width="845" alt="image" src="https://user-images.githubusercontent.com/95380638/187829892-64416941-f1e4-4f95-be0f-5105c3c46c61.png">
  </li>
  <li>
    <p>가계부 목록 조회</p>
    <img width="858" alt="image" src="https://user-images.githubusercontent.com/95380638/187829943-b1710a76-f455-4e27-8d26-872f4f971041.png">
  </li>
  <li>
    <p>특정 가계부 조회</p>
    <img width="850" alt="image" src="https://user-images.githubusercontent.com/95380638/187830002-841a740a-1092-49e4-a580-2551b4b07e75.png">
  </li>
  <li>
    <p>특정 가계부 수정</p>
    <img width="856" alt="image" src="https://user-images.githubusercontent.com/95380638/187830094-bf6c3b30-20a7-4f32-a003-f16c107fd7ef.png">
  </li>
  <li>
    <p>특정 가계부 삭제 및 복구</p>
    <img width="855" alt="image" src="https://user-images.githubusercontent.com/95380638/187830168-446d675e-e8db-4c20-8f38-bbb67cd9ce6b.png">
    <img width="854" alt="image" src="https://user-images.githubusercontent.com/95380638/187830695-dd94e775-717d-4a81-8a75-25fa6500b9ac.png">
  </li>
  <li>
    <p>특정 가계부에 속하는 레코드 생성</p>
    <img width="843" alt="image" src="https://user-images.githubusercontent.com/95380638/187830233-2b08a010-a17e-47b8-83ce-00675cf8699c.png">
  </li>
  <li>
    <p>특정 가계부에 속하는 레코드 목록 조회</p>
    <img width="871" alt="image" src="https://user-images.githubusercontent.com/95380638/187830399-65997557-0640-447b-a815-480c4f50af40.png">
    <img width="860" alt="image" src="https://user-images.githubusercontent.com/95380638/187830422-b191c3bb-6f4c-4f69-869c-b4c8f9dd6a10.png">
  </li>
  <li>
    <p>특정 가계부에 속하는 단일 레코드 조회</p>
    <img width="841" alt="image" src="https://user-images.githubusercontent.com/95380638/187830513-2932f9d6-ae20-4196-b0a9-99ff343c53b1.png">
  </li>
  <li>
    <p>특정 가계부에 속하는 단일 레코드 수정</p>
    <img width="856" alt="image" src="https://user-images.githubusercontent.com/95380638/187830562-78e5f4d3-d9e2-4feb-af4d-9c8888d29c0a.png">
  </li>
  <li>
    <p>특정 가계부에 속하는 단일 레코드 삭제 및 복구</p>
    <img width="860" alt="image" src="https://user-images.githubusercontent.com/95380638/187830627-ed5c03b0-a3b2-458a-9110-78ae8600c94f.png">
    <img width="853" alt="image" src="https://user-images.githubusercontent.com/95380638/187830651-4e85d2de-49d5-4893-a027-f61234cca70c.png">
  </li>

</ul>
</div>
</details>

<br>

## 📋 ERD
<img width="776" alt="image" src="https://user-images.githubusercontent.com/95380638/187832719-1d878354-ab1e-47be-98f9-dea9194cd108.png">

- **User 모델과 Restaurant 모델은 1:N 관계로 설정했습니다. 1명의 유저(사용자)는 여러 개의 식당 또는 가게의 가계부를 생성할 수 있습니다.**
- **Restaurant 모델과 RestaurantRecord 모델은 1:N 관계로 설정했습니다. 1개의 식당은 금액과 메모가 담긴 여러 개의 레코드를 가질 수 있습니다.**
- **삭제는 BooleanField로 완전히 데이터를 삭제하지 않고 True, False로 구분지었습니다.**

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

## ✔️ Test Case
- accounts 앱 : 회원가입 및 회원 로그인 테스트 진행 완료
- restaurant 앱 : 특정 가계부 조회 확인, 특정 가계부에 속한 특정 레코드 조회 확인, 특정 가계부에 속한 레코드 조회 확인 테스트 진행 완료

<br>

## 🌎 배포
- **배포 완료 실패**

- **배포 진행상황**
  - **AWS RDS로 Mysql 5.7버전을 선택하여 데이터베이스 서버 생성 완료**
  - **AWS EC2를 생성하여 해당 EC2와 RDS 연결 완료**
  <img width="1433" alt="image" src="https://user-images.githubusercontent.com/95380638/187838122-899df97b-0106-4a18-871b-61c6d6af06a9.png">
  
  - **루트 디렉터리 내부에 Dockerfile를 생성하여 django 앱 서버에 관련된 도커 이미지를 EC2에서 생성하는 과정에서 오류 발생**
    - 1) mysqlclient가 로컬 환경에서도 mysql 설치 과정에서 오류가 발생했기에 해당 문제라고 판단, 로컬 환경에서 pipenv uninstall mysqlclient를 입력하고 다시 진행 - 실패
    - 2) 로컬 환경의 python 버전이 3.9인데 Dockerfile에서는 3.8로 설정되어 있는 것을 확인하여 FROM python:3.9로 수정 후 다시 진행 - 실패
    - 3) [해당 문서](https://pipenv.pypa.io/_/downloads/en/latest/pdf/)를 찾던 과정에서 pipenv install --deploy 해당 명령어를 찾고 수정 후 다시 진행. 이미지 생성 과정에서 터미널에 어떤 오류도 뜨지 않고 대기 상태가 지속되었기에, 해당 명령어로 Pipfile와 Pipfile.lock 빌드 과정에서 문제가 있다면 빌드에 실패하여 오류가 발생할 수 있도록 하기 위함. - 실패
    - 4) [해당 글](https://github.com/pypa/pipenv/issues/4266)을 참고해서 pipenv install --verbose --deploy --ignore-pipfile 해당 명령어를 찾고 수정 후 다시 진행. pipfile이 문제가 된다면 일단 해당 파일 빌드를 무시하고 진행하려고 했음. - 실패
