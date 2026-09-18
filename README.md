## 📊 CREDIT RISK - Home Credit Default Risk

Projeto de Ciência de Dados focado na previsão de inadimplência de clientes utilizando técnicas de Machine Learning aplicadas ao contexto de Risco de Crédito.

O projeto foi desenvolvido utilizando a base Home Credit Default Risk, disponibilizada pela plataforma Kaggle, com o objetivo de reproduzir um fluxo completo de desenvolvimento de modelos preditivos para identificação de clientes com maior probabilidade de inadimplência.

Ao longo do desenvolvimento foram aplicadas ténicas de análise exploratória, engenharia de variáveis, tratamento de classes desbalanceadas, modelagem, otimização de hiperparâmetros e interpretação dos resultados.


## 🎯 Objetivo

Desenvolver um modelo capaz de estimar a probabilidade de inadimplência de clientes que solicitam crédito, utilizando informações financeiro, demográficas e comportamentais.

O foco principal do projeto foi compreender os fatores associados ao risco de crédito e construir um fluxo completo de Machine Learning alinhado a problemas reais encontrados em instituições financeiras.

## 📊  Dataset

Base utilizada:

**Home Credit Default Risk (Kaggle)**

O projeto foi desenvolvido utilizando exclusivamente a tabela application_train responsável por concentrar as principais informações demográficas, financeiras e cadastrais dos clientes.

Embora a competição disponibilize tabelas auxiliares contendo histórico de crédito, pagamento anteriores e relacionamento financeiro, optou-se por utilizar apenas application_train como objetivo de:

- Desenvolver um pipeline completo de Machine Learning com foco no processo de modelagem
- Permitir maior controle sobre as etapas de análise e engenharia de variáveis
- Reduzir a complexidade inicial do projeto
- Priorizar o entendimento profundo das variáveis principais antes da integração de múltiplas fontes de dados

Essa decisão permitiu concentrar os esforços na construção e interpretação do modelo, mantendo o escopo adequado para um projeto de portifólio.

Limitações:

Informações adicionais presente em tabelas como:

- previus_application
- bureau
- bureau_balance
- installments_payments
- POS_CASH_balance
- credit_card_balance

não foram incorporadas ao processo de modelagem.

A integração dessa fontes pode representar uma evolução futura do projeto, possibilidante capturar aspectos históricos e comportamentais que não estão presentes na base principal.


Principais características:

- Aproximadamente 307 mil observações
- Variáveis financeiras
- Variáveis demográficas
- Variáveis comportamentais
- Variável alvo binária (TARGET)

Distribuição da variável target:

- Adimplentes: ~92%
- Inadimplentes: ~8%

## 🔬Metodologia

O projeto foi desenvolvido seguindo um pipeline completo de Ciência de Dados:

### 1. Análise Exploratória dos Dados (EDA)

- Investigação da variável target
- Análise de valores ausentes
- Avaliação das distribuições numéricas
- Estudo das variáveis categóricas
- Identificação de padrões de inadimplência

### 2. Engenharia de Variáveis

- Criação de flags de missing values
- Imputação numérica e categórica
- Transformações logarítmicas
- One-Hoe Encoding
- Criação de cariáveis derivadas

### 3. Modelo Baseline

- Regressão Logística

### 4. Tratamento do Desbalanceamento

- Class Weight
- SMOTE

### 5. Modelos Avançados

- Random Forest
- XGBoost

### 6. Otimização

- Validação Cruzada
- RandomizedSearchCV
- Ajuste de Threshold


## 🏆 Principais Resultados

| Modelo | Recall Classe 1 | Precision Classe 1 | AUC-ROC |
|----------|----------|----------|----------|
| Logistic Baseline | 0% | 0% | 0.63 |
| Logistic + Class Weight | 57% | 11% | 0.58 |
| Logistic + SMOTE | 44% | 10% | 0.57 |
| Random Forest (Threshold = 0.10) | 59% | 17% | 0.73 |
| XGBoost (Threshold = 0.37) | **74%** | **15%** | **0.758** |

O modelo **XGBoost**, combinado com o ajuste de threshold para **0.37**,
apresentou o melhor equilíbrio entre capacidade de separação das classes
(AUC-ROC) e identificação dos clientes inadimplentes (Recall).


## 🏆 Modelo Final

Após a compração entre diferentes algortimos e estratégias de balanceamento, o modelo XGBoost apresentou o melhor equilíbrio entre Recall, Precision e capacidade de separação entre as classes.

Resultados do modelo final:
- AUC-ROC: 75,8%
- Recall Classe Inadimplente: 74%
- Threshold Final: 0.37

## 🔍 Variáveis Mais Importantes

Os principais fatores associados ao risco de inadimplência foram:

- Indicadores externos de crédito (EXT_SOURCE_2 e EXT_SOURCE_3)
- Escolaridade
- Tipo de renda
- Idade
- Exposição ao crédito
- Variáveis derivadas da estapa de Feature Engineering

## 🚀 Tecnlogias Utilizadas

- Python
- Pandas
- Numpy
- Matplotlib
- Scikit-Learn
- XGBoost
- Jupyter Notebook

## 📁 Estrutura do Projeto

Credit-Risk/

├─ data/

│  └─ application_train.csv <- Base de dados utilizada

│  └─ processed/ Features_processed.csv, Target_processed.csv, top20_features.csv, compracao_modelos.csv, comparacao_modelos.png, top20_features.png <- Features e target pre-processados, tabelas e graficos utilizados ao decorrer do projeto

├─ models/

│ └─ XGB_credit_risk.pkl <- Modelo Campeão

├─ notebooks/

│  └─ 01_eda, 02_feature_engineering, 03_modelo_baseline, 04_modelos_avancados, 05_otimizacao_e_tuning, 06_conclusoes_e_business_insights <- Notebooks desenvolvidos ao decorrer do projeto

├─ requirements/ 

│ └─ requirements.txt <- Dependências do Projeto

└─ README.md <- Documentação do projeto

## 📚 Principais Aprendizados

- Acurácia pode ser enganosa em bases desbalanceadas
- Missing values podem carregar informações relevantes
- O ajuste do trheshold pode ser tão importante quanto a escolha do algortimo
- O entendimento do negocio é fundamental para interpratação das métricas.

## 🔮 Evoluções Futuras

Embora os resultados obtidos tenham sido satisfatórios para os objetivos do projeto, existem diversas oportunidades de evolução que podem ampliar a capacidade preditiva e a aplicabilidade da solução.

Possíveis desenvolvimentos futuros incluem:

- Integração das tabelas auxiliares disponibilizadas pela competição, como bureau, previus_application, install_payments e credit_card_balance
- Criação de novas variáveis comportamentais e agregações históricas relacionadas ao perfil financeiro dos clientes
- Exploração de técnicas mais avançadas de seleção de variáveis e otimização de hiperparâmetros
- Calibração das probabilidades previstas pelo modelo
- Avaliação de métricas de negócio especificas para risco de crédito, incorporando custos associadoas aos diferentes tipos de erro
- Desenvolvimento de um dashboard interarivo utilizando Streamelit para simução de cenários e apoio a tomada de decisão

## Contato
Rodrigo Brito
📧 brito.rd13@gmail.com
💼 https://www.linkedin.com/in/rodrigo-brito-a4393a277/


