import streamlit as st
import pandas as pd



# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title('📌 Navegação')

pagina = st.sidebar.radio(
    'Selecione uma página:',
    [
        '🏠 Sobre o Projeto',
        '📊 Simulador de Crédito',
        '📈 Evolução dos Modelos',
        '🔍 Variáveis Mais Importantes',
        '📚 Metodologia'
    ]
)




# ============================================================
# PÁGINA INICIAL
# ============================================================

if pagina == '🏠 Sobre o Projeto':

    st.title('📊 Credit Risk Predictor')

    st.markdown("""
    Bem-vindo ao dashboard do projeto **Credit Risk - Home Credit Default Risk**.

    Este projeto foi desenvolvido com objetivo educacional e de portfólio,
    utilizando a base **Home Credit Default Risk**, disponibilizada pela Kaggle.

    O desafio consiste em prever a probabilidade de inadimplência de clientes
    que solicitam crédito, utilizando informações financeiras, demográficas
    e comportamentais.

    Ao longo do projeto foram aplicadas técnicas de:

    - Análise Exploratória de Dados (EDA)
    - Engenharia de Variáveis (Feature Engineering)
    - Balanceamento de Classes
    - Modelagem Supervisionada
    - Otimização de Hiperparâmetros
    - Ajuste de Threshold
    - Interpretação das Variáveis Mais Importantes

    Após a avaliação de diferentes algoritmos, o modelo **XGBoost**
    apresentou o melhor desempenho geral.
    """)

    st.divider()

    st.subheader('👨‍💻 Sobre o Projeto')

    st.markdown("""
    Este projeto foi desenvolvido como parte da minha jornada de estudos
    em Ciência de Dados e Machine Learning, com foco em problemas de
    **Risco de Crédito**.

    O objetivo foi reproduzir um fluxo completo de desenvolvimento de um
    modelo preditivo, passando por todas as etapas de um projeto real:

    **EDA → Engenharia de Variáveis → Modelagem → Otimização → Deploy**

    Ao longo do desenvolvimento foram avaliadas diferentes estratégias para:

    - Tratamento do desbalanceamento das classes
    - Ajuste de thresholds de classificação
    - Comparação entre algoritmos
    - Interpretação dos resultados
    - Geração de insights de negócio

    Todo o processo foi documentado em notebooks, relatórios e materiais
    de estudo desenvolvidos durante o projeto.
    """)

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label='AUC-ROC',
            value='75,8%'
        )

    with col2:
        st.metric(
            label='Recall Classe Inadimplente',
            value='74%'
        )

    with col3:
        st.metric(
            label='Threshold Final',
            value='0.37'
        )

    st.success(
        '✅ Modelo Final Selecionado: XGBoost'
    )





# ============================================================
# EVOLUÇÃO DOS MODELOS
# ============================================================

elif pagina == '📈 Evolução dos Modelos':
	st.title('📈 Evolução dos Modelos')
	
	st.markdown(""" 
	Esta seção apresenta a evolução dos modelos avaliados ao longo do projeto.
	
	O objetivo foi identificar a estratégia mais eficaz para previsão de inadimplência, avaliando o impaco do balanceamento das classes,
	ajuste de thresholds e algoritmos mais robustos.

	""")
	
	st.divider()

comparacao = pd.read_csv('data/processed/compracao_modelos.csv')

st.subheader('📋 Comparação dos Modelos')

st.dataframe(comparacao, use_container_width=True)

st.subheader('📊 Evolução do Desempenho')

st.image('data/processed/compracao_modelos.png', use_container_width=True)

st.markdown("""
    ### Principais Conclusões

    - O modelo baseline apresentou elevada acurácia, porém falhou na identificação
      da classe inadimplente.

    - A estratégia `class_weight='balanced'` aumentou significativamente o Recall
      da classe positiva.

    - O SMOTE não produziu ganhos relevantes para este problema.

    - A Random Forest apresentou excelente capacidade de separação (AUC superior
      a 70%), mas necessitou ajuste de threshold.

    - O XGBoost apresentou o melhor equilíbrio entre Recall, Precision e AUC-ROC,
      tornando-se o modelo final selecionado.
    """)





# ============================================================
# VARIÁVEIS MAIS IMPORTANTES
# ============================================================

if pagina == '🔍 Variáveis Mais Importantes':

     st.title('🔍 Variáveis Mais Importantes')
    
     st.markdown("""
     Esta seção apresenta as variáveis que exercem maior influência sobre as previsões realizadas pelo modelo XGBoost.

     A análise permite compreender quais fatores foram mais relevantes para a identificação da probabilidade de inadimplência dos clientes.

    """)



st.divider()
# TOP 20 RANKING GRAFICO

st.subheader('📊 Top 20 Variáveis Mais Importantes')
st.image('data/processed/top20_features.png',use_container_width = True)

# TOP  20TABELA
top20 = pd.read_csv('data/processed/top20_features.csv')
st.subheader('📋 Ranking das Variáveis')
st.dataframe(top20,use_container_width = True)

st.divider()

st.subheader('💡 Principais Insights')

st.info('''
	📌Os indicadores externos de crédito (EXT_SOUCRE_2 e EXT_SOURCE_3 
	apresentaram a maior influência sobre as previsões do modelo,
	reforçando a importância do histórico financeiro para avaliação do risco de inadimplência.)
''')

st.info(
        '''
        📌 Características relacionadas à escolaridade, renda e perfil
        socioeconômico também exerceram influência relevante na segmentação
        dos clientes.
        '''
    )

st.info(
        '''
        📌 Variáveis criadas durante a Engenharia de Features, como
        RATIO_CREDIT_GOODS, apareceram entre os atributos mais importantes,
        demonstrando que a criação de relações financeiras agregou valor
        ao modelo.
        '''
    )

st.info(
        '''
        📌 Flags de valores ausentes também figuraram entre as variáveis
        relevantes, indicando que a ausência de determinadas informações
        contém sinal preditivo útil para avaliação do risco.
        '''
    )

st.success(
        '''
        ✅ Conclusão: o risco de inadimplência não é explicado por uma única
        característica. O modelo identificou uma combinação de fatores
        financeiros, socioeconômicos e comportamentais para distinguir
        clientes de maior e menor risco.
        '''
    )




# ============================================================
# METODOLOGIA
# ============================================================
if pagina == '📚 Metodologia':

    st.title('📚 Metodologia')


# ============================================================
# SIMULADOR DE CRÉDITO
# ============================================================