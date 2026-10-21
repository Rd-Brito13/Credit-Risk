# CRIA O ARQUIVO QUE SERÁ UTILIZADO PARA IMPORTAR AS CLASSES FUTURAMENTE

# IMPORTANDO NOVAMENTE AS BIBLIOTECAS PARA QUE SEJAM ESCRITAS NO ARQUIVO
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

# CRIA A CLASSE QUE SERÁ RESPONSÁVEL PELA CRIAÇÃO DAS VARIAVEIS FLAGS ONDE HOUVER VALOR NAN
class MissingFlagTransformer(BaseEstimator, TransformerMixin):

    # CRIA A FUNÇÃO FIT, RESPONSÁVEL POR RECEBER O DATASET, COLETAR O NOME DAS COLUNAS E ARMAZENAR NA MEMORIA
    def fit(self, features, target = None):

        # ARMAZENA NA MEMORIA (SELF) A LISTA DAS COLUNAS COM VALORES NULOS
        self.colunas_com_missing_ = (features.columns[features.isnull().mean() >0])

        # RETORNA ESSA LISTA NA MEMORIA
        return self
                 # CRIA A FUNÇÃO QUE SERÁ RESPONSAVEL POR REALIZAR A CRIAÇÃO DAS FLAGS A PARTIR DA LISTA DENTRO DE SELF
    def transform(self, features):

        # CRIA UMA COPIA DO DATASET
        features = features.copy()

        # CRIA A ESTRUTURA REPETIÇÃO QUE IRÁ ITERAR DENTRO DA MEMORIA E BUSCAR UMA COLUNA POR VEZ
        for coluna in self.colunas_com_missing_:

            # SE ESTIVER, CRIAR AS COLUNAS FLAGS COM BASE NO NOME DA COLUNA ANTIGO E SE OS VALORES FOREM NAN APLICAR 1 = SIM, 0 = NÃO
            # ATRAVÉS DO ASTYPE(INT)
            features[f'{coluna}_missing_flag'] = features[coluna].isnull().astype(int)

                # RETORNA O DATAFRAME COM FLAGS
        return features
# ADICONA A SEGUNDA CLASSE AO ARQUIVO JÁ CRIADO ANTERIORMENTE

# CLASSE RESPONSAVEL PELA ETAPA DE FEATURE CREATION
class FeatureEngineeringTransformer(BaseEstimator, TransformerMixin):

    # RECEBE O DATASET E ARMAZENA NA MEMORIA
    def fit(self, features, target=None):
        return self

    # CRIA AS NOVAS COLUNAS
    def transform(self, features):
        features = features.copy()

       # REMOVE OS PREXIFOS NOS NOMES DAS COLUNAS QUE SÃO CRIADOS A CADA PASSO APLICADO DO PIPELINE PELO COLUMNTRANSFORMER
        features.columns = [
            col.split('__')[-1] for col in features.columns
        ]


        # EVITANDO DIVISÃO POR ZERO
        features['CNT_FAM_MEMBERS'] = features['CNT_FAM_MEMBERS'].replace(0, 1)

        # FEATURE CREATION
        features['RATIO_CREDIT_INCOME'] = features['AMT_CREDIT'] / (features['AMT_INCOME_TOTAL'] + 1)
        features['RATIO_ANNUITY_INCOME'] = features['AMT_ANNUITY'] / (features['AMT_INCOME_TOTAL'] + 1)
        features['CREDIT_PER_PERSON'] = features['AMT_CREDIT'] / (features['CNT_FAM_MEMBERS'] + 1)
        features['INCOME_PER_PERSON'] = features['AMT_INCOME_TOTAL'] / (features['CNT_FAM_MEMBERS'] + 1)
        features['RATIO_CREDIT_GOODS'] = features['AMT_CREDIT'] / (features['AMT_GOODS_PRICE'] + 1)

        # LOG TRANSFORM (Corrigido de 'X' para 'features')
        features['AMT_INCOME_TOTAL_log'] = np.log1p(features['AMT_INCOME_TOTAL'])
        features['AMT_CREDIT_log'] = np.log1p(features['AMT_CREDIT'])
        features['AMT_GOODS_PRICE_log'] = np.log1p(features['AMT_GOODS_PRICE'])
        features['AMT_ANNUITY_log'] = np.log1p(features['AMT_ANNUITY'])

        features = features.drop(columns = ['AMT_INCOME_TOTAL','AMT_CREDIT','AMT_GOODS_PRICE','AMT_ANNUITY'])

        # RETORNA O DATASET
        return features
