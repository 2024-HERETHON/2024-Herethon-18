# 2024-Herethon-18
2024 여기톤 : HERETHON 18조
## 서비스 소개
SW정책연구소(SPRi)가 발간한 '2022년 SW산업 실태조사' 보고서에 따르면 2022년 국내 테크기업의 SW부문에서 근무하는 인원 수는 50만명 이상을 기록했고, 전년 대비 13.8% 늘어난 수치다. 또한 개발자 커뮤니티의 이용자도 증가하고 있는 추세다. 2023년, 개발자 커뮤니티 '커리어리'의 누적 이용자수가 30만명을 넘어섰고, 마이크로소프트도 개발자 커뮤니티의 성장을 돕고 있다.

[서비스 이름]은 개발자 수와 커뮤니티 사용자 수가 증가하고 있는 현재, 포트폴리오보다 솔직한 프로젝트 피드백과 감상을 남기고 공유하면서 부족한 점을 보완하는 데 도움을 준다. 기존에 있는 깃허브와 달리 본인이 과거 작성했던 게시물에 대해 감상을 남기고 회고할 수 있으며, 깃 블로그에 남기기에 개인적인 감상 같은 서술도 작성할 수 있다. 디스콰이엇과 달리 개발 프로젝트 공유에 초점을 맞춘 점도 존재한다.(주목할 만하다)

---
## 서비스 제공 기능과 사용방법
[서비스 이름]은 서브메뉴로 공유용 게시판, 성장 관찰, 마이페이지가 존재한다. '공유용 게시판' 메뉴에서는 사용자의 프로젝트 게시물을 작성할 수 있고 다른 사용자의 게시물도 열람할 수 있다. 게시물에는 개발 기간, 참여 인원수, 사용 언어를 드롭다운으로 선택할 수 있다. 프로젝트 목적과 같은 프로젝트 설명, 배포 링크, 깃허브 주소는 줄글로 작성 가능하며 협업자는 '@' 기호를 이용하여 멘션 가능하다. 다른 사용자의 게시물에는 '좋아요'와 '아쉬워요' 버튼을 이용해서 간단히 본인의 감상을 남길 수 있고, 상세하게 피드백을 주고 싶다면 댓글 기능을 이용하여 전달할 수 있다.


'성장 관찰' 메뉴에서는 사용자가 현재 접속 시점까지 업로드한 총 포스트의 개수, 포스트에 받은 좋아요 개수, 최근 5개 게시물에 대한 [좋아요/조회수] 비율을 통한 성장 그래프(이하 '성장 History'), 회고글 작성을 할 수 있다. 총 포스트 개수, 좋아요 개수, 성장 History는 자동으로 업데이트되며 사용자가 수정할 수 없다. 사용자는 '성장 관찰' 메뉴에서 회고 글을 작성하는 액션을 취할 수 있다. 회고글을 작성할 때는 2분할 화면이 보이며 좌측 분할 화면에는 과거에 작성한 프로젝트 게시물이 댓글창과 함께 표시되고, 우측 분할 화면에는 회고글을 작성할 수 있는 칸이 표시된다. 사용자는 과거 게시물과 댓글을 통한 피드백을 동시에 확인하고 참고하면서 회고글을 작성할 수 있다. 사용자가 프로젝트 게시물을 작성한지 30일이 지났을 때, 로그인 이후 홈 화면에 회고글을 작성하는 것을 제안하는 팝업창이 표시된다.

다른 사용자의 게시물에 대한 반응, 게시물 작성, '성장 관찰' 메뉴 이용을 위해서는 로그인이 필요하다. 로그인 방법으로 카카오톡 로그인과 네이버 로그인을 포함한 소셜 로그인과 웹사이트 자체 회원가입을 통한 로그인이 존재한다. 상단바의 '마이페이지'를 클릭하여 로그인과 부가 기능을 사용할 수 있다. 마이페이지에 접속하면 세부 메뉴로 '회고용 게시물 공유', '환경설정', '계정 삭제'가 존재한다. '회고용 게시물 공유'를 클릭해서 회고글을 공유하는 범위를 모두 공개, 친구 공개, 나만 보기 중 선택할 수 있다. 친구 공개를 통해 친구와 회고 게시글을 공유하고 싶다면 친구의 아이디나 이메일을 추가해서 공유할 수 있다. 초대한 친구들은 친구 추가 칸 아래에서 확인 가능하다. 다음 세부 메뉴로 '환경설정'을 클릭하면 다른 사용자에 의해 협업자로 멘션되었을 때의 알림 수신에 대한 동의 선택, 비밀번호 변경을 할 수 있다.

---
## 기술 스택
  - 프론트엔드: HTML, CSS, JS
  - 백엔드:
  - 기획.디자인: 피그마
---


## 팀원 소개


|**김나영**|**김세은**|**남지연**|**백지원**|**윤나경**|**한정현**|
|:---:|:---:|:---:|:---:|:---:|:---:|
|백엔드|백엔드|프론트엔드|기획&디자인|프론트엔드|프론트엔드|
| 성장 관찰 페이지 기능 구현 | 공유용 게시판 기능 구현 | 성장 관찰 페이지 구현 | 와이어프레임 작성 | 공유용 게시판 페이지 구현 | 마이페이지 구현 |
| 마이페이지 기능 구현 | reflect 작성, 게시 기능 구현 | 회고하러 가기 페이지 구현 | UI 디자인 | reflect 작성 페이지 구현 | 회원가입, 로그인 페이지 구현 |
| 회고하러 가기, 회고 게시 기능 구현 |  | 팝업창 기능 구현  |  발표 PPT 제작 |  |  | ProReflect 게시 페이지 구현 |

---


## 폴더 구조

[작성 필요]

📂 2024-Herethon-18 <br/>
└─ project <br/>
 ├─ myapp <br/>
 <ul>
 │  ├─ __pycache__ <br/>
 │  ├─ migrations <br/>
 │  ├─ templates <br/>
 </ul>
    <ul>   ├─ after_login.html <br/>
       ├─ board_create.html <br/>
       ├─ board_detail.html <br/>
       ├─ board_list.html <br/>
       ├─ board_update.html <br/>
       ├─ grow_1.html <br/>
       ├─ grow_2.html <br/>
       ├─ grow_3.html <br/>
       ├─ home_search.html <br/>
       ├─ login_create.html <br/>
       ├─ login.html <br/>
       ├─ main.html <br/>
       ├─ mypage_setting.html <br/>
       ├─ mypage_share.html <br/>
       ├─ new_login_home.html <br/>
       ├─ retrospective.html <br/>
       └─ signup.html <br/>   </ul> 
 │  ├─ templatetags <br/> 
 <ul>
       ├─ __pycache__ <br/>
       └─ myapp_filters.py <br/> </ul>
    ├─ __init__.py <br/>
    ├─ admin.py <br/>
    ├─ apps.py <br/>
    ├─ forms.py <br/>
    ├─ models.py <br/>
    ├─ tests.py <br/>
    ├─ urls.py <br/>
    ├─ userSave.py <br/>
 │  └─ views.py <br/>
 ├─ myenv <br/>
  <ul> ├─ Include <br/>
    ├─ Lib\site-packages <br/>
    ├─ Scripts <br/>
    └─ pyvenv.cfg <br/> </ul>
 ├─ project <br/>
 
 <ul>  ├─ __pycache__ <br/>
    ├─ __init__.py <br/>
    ├─ asgi.py <br/>
    ├─ settings.py <br/>
    ├─ urls.py <br/>
    └─ wsgi.py <br/> </ul>
 ├─ static <br/> 
<ul>    ├─ css <br/>
       ├─ after_login.css <br/>
       ├─ board_create.css <br/>
       ├─ board_detail.css <br/>
       ├─ board_list.css <br/>
       ├─ grow_1.css <br/>
       ├─ grow_2.css <br/>
       ├─ home_search.css <br/>
       ├─ home.css <br/>
       ├─ login.css <br/>
       ├─ mypage_setting.css <br/>
       ├─ mypage_share.css <br/>
       ├─ reset.css <br/>
       ├─ signup.css <br/>
       └─ style.css <br/> </ul>
    ├─ img <br/>
     <ul>  ├─ back-button.svg <br/>
       ├─ board-search.svg <br/>
       ├─ default_project_image.png <br/>
       ├─ heart-clicked.svg <br/>
       ├─ heart.svg <br/>
       ├─ inverted-triangle.svg <br/>
       ├─ kakao_login.png <br/>
       ├─ naver_login.png <br/>
       ├─ paperclip.svg <br/>
       ├─ person.png <br/>
       ├─ QuestionMark.svg <br/>
       ├─ water-drop-clicked.svg <br/>
       └─ water-drop.svg <br/> </ul>
    └─ js <br/>
    <ul>
       ├─ board_create.js <br/>
       ├─ board_list.js <br/>
       ├─ home_search.js <br/>
       ├─ home.js <br/>
       ├─ mypage_setting.js <br/>
       └─ mypage_share.js <br/> </ul>
 ├─ uploads <br/>
 <ul>
    ├─ default-profile.jpg <br/>
    └─ IMG_1585.jpeg <br/> </ul>
 ├─ db_backup.json <br/>        
 ├─ db.sqlite3 <br/>
 ├─ manage.py <br/>
 ├─ .gitignore <br/>
 ├─ db_backup.json <br/>
 └─ README.md <br/>
---


## 개발 환경에서의 실행 방법

django-admin startproject 프로젝트명 <br/>
python manage.py runserver
---


## References
### '서비스 소개' 참고 기사
1. MS, AI 변화의 중심은 '개발자'...국내 개발자 커뮤니티 성장 지원<https://www.gttkorea.com/news/articleView.html?idxno=10238>
2. 5년간 소프트웨어 인력 규모 늘었지만...테크업계, 전문 인력 부족에 쩔쩔 <https://www.ajunews.com/view/20230706144014851>
