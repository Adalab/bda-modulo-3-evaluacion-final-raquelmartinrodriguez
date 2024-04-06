#%%
from src import soporte as sp
import pandas as pd

#CARGAMOS LOS CSV
df_activity = pd.read_csv('files/customer_flight_activity.csv')
df_loyalty = pd.read_csv('files/customer_loyalty_history.csv')

#EXPLORAMOS LOS CSV
sp. explorar_df (df_activity, df_loyalty)

# %%
