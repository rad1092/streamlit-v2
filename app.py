import streamlit as st

st.set_page_config(
    page_title="스마트홈 대시보드 - 김홍대",
    layout = "wide",
)

st.header("스트림릿 배포 테스트중")
st.write("스트림릿 배포 해보기-김홍대")

# 페이지 등록
# st.Page("파일경로", title = "메뉴 이름", icon = "아이콘명")
# 1. 홈 화면
home = st.Page("pages/home.py", title = "홈")
# 2. 센서 화면
sesnors = st.Page("pages/sensors.py", title = "센서 데이터")
# 3. 전력 화면
power = st.Page("pages/power.py", title = "전력 현황")
# 4. 온도 분석 화면
temperature = st.Page("pages/temperature.py", title = "온도 분석")
# 네비게이션 구성
pg = st.navigation({
    "메인" : [home],
    "분석" : [sesnors, power],
    "온도분석" : [temperature]
})

st.sidebar.write("같은 사이드바 형태입니다")

# 선택된 페이지를 실행
pg.run()