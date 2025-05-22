import pandas as pd
dfParquet = pd.read_parquet(r'C:\Users\UNSAAC\Desktop\facil sirve despues\ORACLE\ChallengeTelecomX\df_final_limpio.parquet');
columnas_deseadas = [
    'customerID','Churn','gender','SeniorCitizen', 'Partner', 'Dependents', 'tenure',
    'PhoneService', 'MultipleLines',
    'InternetService', 'OnlineSecurity', 'OnlineBackup',
    'DeviceProtection', 'TechSupport',
    'StreamingTV', 'StreamingMovies',
    'Contract', 'PaperlessBilling', 'PaymentMethod',
    'Charges.Monthly', 'Charges.Total'  
]
columnas_booleanas = [
    'Churn','Partner','Dependents','PhoneService','MultipleLines',
    'OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport',
    'StreamingTV','StreamingMovies','PaperlessBilling'
]
"""dfParquet['Cuentas_Diarias'] = dfParquet['Charges.Monthly']/30;
print(dfParquet[columnas_deseadas].iloc[0])"""
#CONVIRTIENDO CADA COLUMNA BOOLEANA A UNA DE 1 Y 0
'''for col in columnas_booleanas :
    dfParquet[col]= (
        dfParquet[col]
        .astype(str)
        .str.lower()
        .map({"yes":1,"no":0})
        .fillna(0)
        .astype(int)
    )
'''
import numpy as np
mediaMonthly = np.mean(dfParquet['Charges.Monthly'])
mediaTotal = np.mean(dfParquet['Charges.Total'])
medianaMonthly = np.median(dfParquet['Charges.Monthly'])
medianaTotal = np.median(dfParquet['Charges.Total'])
desviacionEstandarMonthly = np.std(dfParquet['Charges.Monthly'])
desviacionEstandarTotal = np.std(dfParquet['Charges.Total'])  
varianzaMonthly = np.var(dfParquet['Charges.Monthly'])
varianzaTotal = np.var(dfParquet['Charges.Total'])
rangoMonthly =np.max(dfParquet['Charges.Monthly']) - np.min(dfParquet['Charges.Monthly'])
rangoTotal =np.max(dfParquet['Charges.Total']) - np.min(dfParquet['Charges.Total'])

from scipy.stats import mode
modaMonthly = mode(dfParquet['Charges.Monthly'], keepdims=True)
modaTotal = mode(dfParquet['Charges.Total'], keepdims=True)