#%%
from src import soporte as sp
import pandas as pd

# CARGAMOS LOS CSV
df1 = sp.abrir_csv('files/customer_flight_activity.csv')
df2 = sp.abrir_csv('files/customer_loyalty_history.csv')

# EXPLORAMOS LOS CSV
sp.explorar_df(df1, df2)

# %%
