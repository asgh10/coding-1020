import streamlit as st

# 파이썬 안에서 CSS 스타일을 적용하는 맛보기 코드
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)