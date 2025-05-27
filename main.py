import FinanceDataReader as fdr
import streamlit as st
import datetime 

with st.sidebar:
    date = st.date_input("조회 시작(일)을 선택해 주세요.", datetime.date(2024, 1, 1))
    code = st.text_input('종목 코드', value='', placeholder='종목코드를 입력해 주세요.')

if code and date :
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:,'Close']
    tab1 , tab2 = st.tabs(['차트', '데이터'])

    with tab1:
        st.line_chart(data)
    with tab2:
        st.dataframe(df.sort_index(ascending=False))
    with st.expander('컬럼 설명'):
        st.markdown(''' 
        - open: 시가
        - high: 고가
        - low: 저가
        - close: 종가
        - Adj Close: 수정 종가
        - volume: 거래량
        ''')