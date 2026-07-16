
import streamlit as st
import pandas as pd

header = ['학번','이름','전공']

if 'students' not in st.session_state:
    st.session_state.students = [
        ['202601', '홍길동', '컴퓨터공학'],
        ['202602', '이순신', '데이터사이언스'],
        ['202603', '유관순', '인공지능학'],
    ]

# 타이틀
st.title('학생 정보 등록하기')

# 학생 정보 입력 form
stu_id = st.text_input('학번을 입력하세요.')
stu_name = st.text_input('이름을 입력하세요.')
stu_major = st.text_input('전공을 입력하세요.')

# 등록하기 버튼
if st.button('등록'):
    if stu_id and stu_name and stu_major:
        st.session_state.students.append([stu_id, stu_name, stu_major])
        st.success(f'{stu_name} 학생이 등록되었습니다.')

df = pd.DataFrame(st.session_state.students, columns=header)
st.table(df)
