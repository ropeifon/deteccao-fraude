# Projeto: Previsão e análise de fraude em transações de cartão de crédito
 Fomos contratados por um dos maiores bancos do país, o Banco Seguro (nome fictício), como cientista e analista de dados para ajudar a combater o aumento alarmante de fraudes em transações de cartão de crédito. Em uma reunião inicial com a equipe de segurança e prevenção de fraudes do banco, ficou claro que a situação atual está se tornando insustentável, com perdas financeiras significativas e uma crescente desconfiança por parte dos clientes.

# Objetivo 

O objetivo é **analisar os dados e identificar padrões nas transações suspeitas** e  **desenvolver um sistema de detecção de fraudes** altamente eficaz que possa identificar transações suspeitas em tempo real. Isso requer a análise de grandes volumes de dados de transações de cartão de crédito em busca de padrões incomuns ou atividades fraudulentas.

# Detalhes do Projeto

Neste projeto, iciamos com uma base de dados (arquivo .csv) com alguns dados do problema. Passamos por várias etapas ao longo de toda a exploração do projeto, são elas: 

+ Análise exploratória dos dados com o objetivo de identificar como os dados estão se comportando.
+ Tratamento de valores inconsistentes e valores faltantes.
+ Análise descritiva das variáveis.
+ Análise de correlação entre as variáveis
+ Uso da estatística inferencial para testar hipótese
+ Processo de criação de novas features
+ Transformação das variáveis categóricas com o CatBoost Encoder
+ Escalonamento das variáveis numéricas com o StandardScaler
+ Desenvolvimento de diversos modelos de aprendizado supervisionado como Regressão Logística, Árvore de Decisão, Floresta Aleatória, XGBoost e LightGBM
+ Balanceamento dos dados utilizando a abordagem SMOTE vs hiperparâmetros de balanceamento dos dados do próprio XGBoost e LightGBM
+ Utilização da validação cruzada para escolha do modelo
+ Ajuste de hiperparâmetros com a ajuda do framework Optuna
+ Visualizações de métricas como Recall, F1-score e ferramentas como a Curva ROC e a Matriz de Confusão para averiguar o desempenho do modelo
+ Criação de um pipeline para previsão em novos dados
+ Deploy do modelo
+ Bônus: Redes Neurais Profundas e Voting Classifier)

## Status do projeto: 

> 90% finalizado.

O que ainda será feito no projeto? Será adicionado um dashboard interativo no aplicativo para que a equipe de segurança possa visualizar os dados de uma forma precisa e consistente. O modelo também pode ser melhorado, isto é, podemos criar novas features e realizar análise também de Feature Importance. Todas estas melhorias serão adicionadas ao longo do tempo. 

# Link do aplicativo

[O aplicativo pode ser acessado clicando aqui](https://deteccao-fraude-robpeifon.streamlit.app)
