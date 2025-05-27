import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

dfParquet = pd.read_parquet(r'C:\Users\UNSAAC\Desktop\facil sirve despues\ORACLE\ChallengeTelecomX\df_final_limpio.parquet');

variablesNumericas= ['tenure', 'Charges.Monthly', 'Charges.Total']
VariablesCategoricas = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents',
    'Contract', 'PaymentMethod', 'PaperlessBilling',
    'InternetService', 'OnlineSecurity', 'TechSupport'
]

st.title("Análisis de Cancelación de Clientes (Churn)");
tipoAnalisis = st.radio("¿Qué tipo de variable quieres analizar?", ['Numérica', 'Categórica']);

if tipoAnalisis == 'Numérica':
    VariablesSeleccionadas = st.selectbox("Selecciona una variable numérica:", variablesNumericas);
    fig = px.histogram(dfParquet, x=VariablesSeleccionadas, color='Churn', marginal='box',
                       nbins=40, title=f'Distribución de {VariablesSeleccionadas} según Churn')
    
    stats = dfParquet.groupby('Churn')[VariablesSeleccionadas].agg(['mean', 'median']).reset_index()
    st.plotly_chart(fig)
    st.subheader("Media y Mediana por grupo Churn")
    st.dataframe(stats)

elif tipoAnalisis == 'Categórica':
    VariablesSeleccionadas = st.selectbox("Selecciona una variable categórica:", VariablesCategoricas)

    fig = px.histogram(dfParquet, x=VariablesSeleccionadas, color='Churn', barmode='group',
                       title=f'Distribución de Churn según {VariablesSeleccionadas}', text_auto=True)
    st.plotly_chart(fig)

    st.subheader("Porcentajes de Cancelación por Categoría")
    churn_percent = dfParquet.groupby([VariablesSeleccionadas, 'Churn']).size().reset_index(name='count')
    total = churn_percent.groupby(VariablesSeleccionadas)['count'].transform('sum')
    churn_percent['percentage'] = churn_percent['count'] / total * 100
    st.dataframe(churn_percent)