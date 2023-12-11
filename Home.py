import streamlit as st
import polars as pl
from streamlit_echarts import st_echarts
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import json

st.set_page_config(
    page_title="Financial",
#    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(
    """ <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """,
    unsafe_allow_html=True,
)
with open ('style.css') as f:
			st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
                     
st.sidebar.selectbox('Escolha uma ação', ['VGIA11'])
st.sidebar.date_input('Data incial')
st.sidebar.date_input('Data Final')



col1x,col2x,col3x,col4x,col5x = st.columns(5)

with col1x:
    st.metric('Valor Atual', '9,37','8,8')

with col2x:
    st.metric('Min', '8,8')

with col3x:
    st.metric('Max', '10,64' )

with col4x:
    st.metric('Dy', 42)

with col5x:
    st.metric('Rendimento Médio', '0,14')         

col6x,col7x,col8x,col9x,col10x = st.columns(5)

with col6x:
    st.metric('Último Rendimento', '0,13')

with col7x:
    st.metric('N Cotista', '138.563')

with col8x:
    st.metric('P/VP', '0,99' )

with col9x:
    st.metric('Dp', '0,02')

with col10x:
    st.metric('Cv', '0,002')         



options = {
    #"title": {"text": "Controle de gastos", "subtext": "", "left": "center"},
    "tooltip": {"trigger": "item"},
    "legend": {"top": "top"},
    "series": [
        {
            #"name": "访问来源",
            "type": "pie",
            "radius": "50%",  # Ajuste os valores de raio conforme necessário
            "data": [
                {"value": 1048, "name": "Salário"},
                {"value": 735, "name": "Luz"},
                {"value": 580, "name": "Cartão de crédito"},
                {"value": 484, "name": "Gasolina"},
                {"value": 300, "name": "Saldo"},
            ],
            "label": {
                "show": True,
                "formatter": "{b}: {c} ({d}%)",  # {b} representa o nome, {c} o valor, {d} a porcentagem
            },            
            "emphasis": {
                "itemStyle": {
                    "shadowBlur": 10,
                    "shadowOffsetX": 0,
                    "shadowColor": "rgba(0, 0, 0, 0.5)",
                }
            },
        }
    ],
}


col1,col2 = st.columns([3,3])

with col1:
    st.info('**Controle de gastos**')   
    st_echarts(
    options=options, height="600px",
    )

with col2:
    
    sequencia = pd.Series(range(1, 23))

    valores_aleatorios = np.random.rand(22)
   
    
    st.info('**Fechamento de ações**')
    option2 = {
    "xAxis": {
        "type": "category",
        "data": eval(sequencia.to_json(orient='records')[1:-1]),
    },
    "yAxis": {"type": "value"},
    "series": [{"data": json.dumps(valores_aleatorios.tolist()), "type": "line"}],
    }
    st_echarts(
    options=option2, height="500px",
    )