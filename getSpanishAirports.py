import pandas as pd
import pickle

# URL of the table
url = "https://aeropuertos.wordpress.com/2011/02/27/listado-aeropuertos-espana/"

tablas = pd.read_html(url)

df_aeropuertos = tablas[0]

print(df_aeropuertos.head())

print("Length: ", len(df_aeropuertos))

with open("spanish_airports.pkl", "wb") as f:
    pickle.dump(df_aeropuertos, f)

print("The table was correctly saved")
