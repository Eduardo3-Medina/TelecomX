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


