###############################################################################################################
########## GOSTARIA DE AGRADECER @SarahBarbosa POR TER ME ILUMINADO NO QUE DIZ RESPEITO AO STREAMLIT ##########

import streamlit as st 
import pandas as pd 
import joblib
import matplotlib.pyplot as plt 
import holidays
import datetime
import plotly.express as px
import plotly.graph_objs as go
import time

###############################################################

# Carregando o modelo 
modelo = joblib.load('modelo_xgboost.pkl') # Estou usando o melhor modelo que eu obtive resultados (score = 0.95 no Kaggle)

# Carregando a base de dados 

colunas = pd.read_csv('treino_tratado.csv').columns[1:] # A variável alvo "is_fraud" está na posição 0. Removendo-a.

treino = pd.read_csv('treino_tratado.csv')

cidades_disponiveis = treino['city'].unique()
estados_disponiveis = treino['state'].unique()

###############################################################


# Dados para previsão 
def fazer_previsao(dados_de_entrada):
    df_entrada = pd.DataFrame([dados_de_entrada], columns = colunas)
    predicao = modelo.predict(df_entrada)
    predicao_prob = modelo.predict_proba(df_entrada)[:, 1]
    return predicao[0], predicao_prob[0]

###############################################################

# Exibindo a previsão

def exibir_previsao(dados_de_entrada):
   predicao, predicao_prob = fazer_previsao(dados_de_entrada)
   probabilidade_porcentagem = round(predicao_prob, 3) * 100

   coluna1, coluna2 = st.columns([1, 2])

   mensagem = f"<p style='font-size: 24px;; color: {'red' if predicao_prob >= 0.5 else 'green'};'>"
   mensagem += f"Esta transação <span style='font-weight: bold;'>{'tem uma alta probabilidade de ' if predicao_prob >= 0.5 else 'tem uma alta probabilidade de não '}"
   mensagem += "ser fraude</span></p>"

   with coluna1:
        st.header('Probabilidade da transação ser fraude')
        st.markdown(mensagem, unsafe_allow_html=True)

   with coluna2:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            number={'suffix': "%", 'font': {'size': 50}},
            value=round(predicao_prob, 3) * 100,
            gauge={'axis': {'range': [0, 100], 'tickvals': [0, 25, 50, 75, 100],
                            'ticktext': ['MÍNIMA', 'BAIXA', 'MÉDIA', 'ALTA', 'MÁXIMA'],
                            'tickwidth': 0.1, 'tickfont': {'size': 16, 'color': 'black'}},
                'bar': {'color': 'black'},
                'steps': [{'range': [0, 25], 'color': "#007A00"},
                            {'range': [25, 50], 'color': "#0063BF"},
                            {'range': [50, 75], 'color': "#FFCC00"},
                            {'range': [75, 100], 'color': "#ED1C24"}]
        }))
        
        st.plotly_chart(fig, use_container_width=True)


###############################################################
    
colunas_st = st.sidebar.selectbox(
     'Selecione o que você deseja',
     ('Introdução', 'Predição')
)

###############################################################

if colunas_st == 'Introdução':
    st.title('Detector de fraudes')
    st.caption('Este aplicativo foi desenvolvido para detectar fraudes em transações de cartão de crédito.')
    st.text('Use a coluna ao lado esquerdo para fazer as previsões')
    st.text('OU') 
    st.text('visualizar o relatório sobre fraudes')

   

if colunas_st == 'Predição':
   st.title('Área de previsão.')
    # Entradas do usuário
   st.header('Informações do cliente')

   coluna1, coluna2, coluna3, coluna4, coluna5 = st.columns(5)

   with coluna1: 
        cc_num = st.number_input('Número do cartão:', format='%d', step = 1)

   with coluna2: 
        job = st.text_input('Emprego', '')
    
   with coluna3:
       idade = st.number_input('Idade em anos', format='%d', step = 1)
   
   with coluna4:
       acct_num = st.number_input('Número da conta',format='%d', step = 1)

   with coluna5: 
       gender = st.radio('Gênero', ['M', 'F'])

      
   st.header('Informações geográficas do cliente')

   coluna1, coluna2, coluna3, coluna4, coluna5, coluna6 = st.columns(6)

   with coluna1: 
       state = st.selectbox('Estado (UF)', estados_disponiveis)

   with coluna2: 
       cidade = st.selectbox('Cidade', cidades_disponiveis)

   with coluna3: 
       city_pop = st.number_input('População (city)', format='%d', step = 1)

   with coluna4: 
       street = st.text_input('Rua', '')
       st.markdown('ex: 097 Alexandria Stravenue')

   with coluna5: 
       lat = st.number_input('Latitude')

   with coluna6: 
       long = st.number_input('Longitude')
       

   st.header('Informações do comerciante')

   coluna1, coluna2= st.columns(2)
 
   with coluna1: 
       category = st.text_input('Categoria (ex: misc_pos)', '')
   
   with coluna2: 
       merchant = st.text_input('Nome do comerciante (ex: fraud_Thiel PLC)', '')
    
   st.header('Quantidade transacionada')
   amt = st.number_input('Escreva um alcance de valor')

   
   st.header('Informações temporais')

   coluna1, coluna2, coluna3, coluna4 = st.columns(4)
 
   with coluna1: 
       unix_time = st.number_input('Tempo Unix')
   with coluna2: 
       dia_semana = st.number_input('Dia da semana', format='%d', step = 1)
       st.markdown('0: domingo, 1: segunda, 2: terça, 3: quarta, 4: quinta, 5: sexta, 6: sábado')
   with coluna3: 
       feriado = st.number_input('Feriado?', format='%d', step = 1)
       st.markdown('0: Não, 1: Feriado')
   
   with coluna4: 
       hora = st.number_input('Hora do dia', format='%d', step = 1)
       st.markdown('ex: 22, 23, 24')
    
   dados_de_entrada = {
        'cc_num': cc_num,
        'job': job,
        'idade': idade,
        'acct_num': acct_num,
        'gender': gender,
        'state': state,
        'city': cidade,
        'city_pop': city_pop,
        'street': street,
        'lat': lat,
        'long': long,
        'category': category,
        'merchant': merchant,
        'amt': amt,
        'unix_time': unix_time,
        'dia_semana': dia_semana,
        'feriado': feriado,
        'hora': hora
   }

   if st.button('Ver Previsão'):
        with st.spinner('Fazendo a previsão...'):
            time.sleep(3)
            exibir_previsao(dados_de_entrada)
