#%%
import pandas as pd
#%%
def explorar_df(df1, df2):
    # Exploración del primer DataFrame (df1)
    print("DataFrame 1:")
    print(f"Número de filas: {df1.shape[0]} | Número de columnas: {df1.shape[1]}")
    print("-------------------------")
    print("Principales estadísticos:")
    print(df1.describe().T)
    print("-------------------------")
    print("Porcentaje de valores nulos en cada columna:")
    print(df1.isna().sum() / df1.shape[0] * 100)
    print("-------------------------")
    print("Número de filas duplicadas:")
    print(df1.duplicated().sum())
    print("-------------------------")
    print("Información sobre tipos de datos:")
    print(df1.info())
    print("-------------------------")

    # Exploración del segundo DataFrame (df2)
    print("DataFrame 2:")
    print(f"Número de filas: {df2.shape[0]} | Número de columnas: {df2.shape[1]}")
    print("-------------------------")
    print("Principales estadísticos:")
    print(df2.describe().T)
    print("-------------------------")
    print("Porcentaje de valores nulos en cada columna:")
    print(df2.isna().sum() / df2.shape[0] * 100)
    print("-------------------------")
    print("Número de filas duplicadas:")
    print(df2.duplicated().sum())
    print("-------------------------")
    print("Información sobre tipos de datos:")
    print(df2.info())

#%% 


   

   
# %%
