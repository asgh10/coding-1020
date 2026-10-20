import streamlit as st
import datetime

st.title("✈️ 나의 여행 D-Day 계산기") # 웹 브라우저 화면 맨 위에 큼직한 제목(Title)을 표시해 준다 ( html에서는 마치 h1 같이 )

travel_name = st.text_input("어디로 여행을 가시나요?", "한국") # st.text_input: 사용자가 글자를 입력할 수 있는 텍스트 상자를 만든다 (기본값으로 "스위스"가 들어가도록 설정되어 있다)
travel_date = st.date_input("여행 출발일을 선택해주세요") # st.date_input: 사용자가 마우스로 클릭해서 날짜를 고를 수 있는 달력 형태의 입력창을 만들어 준다

if st.button("D-Day 계산하기"): # st.button: 화면의 누를 수 있는 버튼 한개를 만들고 이 버튼을 누른다면 아래 코드들을 실행한다
    today = datetime.datetime.now().date() # 이 코드로 오늘 날짜를 구하고
    remaining = travel_date - today # 사용자가 선택한 거에서 오늘을 뺀 후 남은 날짜를 계산한다
    
    if remaining.days > 0:
        st.success(f"{travel_name} 출발까지 **{remaining.days}일** 남았습니다!") # 출발까지 남았다면 초록색 박스로 남은 일수를 
    elif remaining.days == 0:
        st.balloons() # 당일이라면 폭죽효과도 같이 넣어준다
        st.success("드디어 오늘이 여행 당일입니다! 즐거운 여행 되세요!")
    else:
        st.error("선택하신 여행일이 이미 지났습니다.") # 이미 날짜가 지났다면 경고문을 띄운다

'''
초록색 (성공/완료): st.success("메시지")

파란색 (일반 안내): st.info("메시지")

노란색 (주의/경고): st.warning("메시지")

빨간색 (에러/지나간 날짜 등): st.error("메시지")

보통 많이 쓰이는 색깔 박스 코드
'''