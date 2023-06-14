import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("cancer.csv",index_col="id")
print(df)

filas = df.head()
print("\n Se mostrará solo las primeras 5 filas \n", filas)

filas_diez = df.head(10)
print("\n Se mostrará solo las primeras 10 filas \n",filas_diez)

ult_filas = df.tail(8)
print("\n Se mostrará solo las últimas 8 filas \n", ult_filas)

estadistica = df.describe()
print("Se mostrará una nueva matriz con las estadísitcas descriptivas de cada columna", estadistica)

#dropna quita las filas con valores nulos, creo que quitó todas las filas xd
filtrado = df.dropna()
print("\n Matriz limpia \n", filtrado)

#cambio de valores de nulos a 0
cambio = df.fillna(0)
print("\n Valores nulos cambiados por 0 \n", cambio)

"""también se pueden cambiar valores por columnas
y se haría mediante un diccionario: 
df.fillna({"radius_mean":0, "perimeter_mean":1})"""

#selecciono los datos de una sola columna
col = df["radius_mean"]
print("\n Accedo solo a los datos de esa columna \n", col)

#filtro por condiciones, en este caso que el radio sea mayor que 27u
print("\n Filtro por \n", df[df["radius_mean"]>27])

#agrupar por columnas
print("Conteo de los tipos de cáncer")
grupo = df["diagnosis"].groupby(df["diagnosis"]).count()
print(grupo)
grupo.plot(kind='pie')
plt.show()

#Máximo valores
print("Máximo valores")
maxi = df.groupby(df["diagnosis"]).max()
print(maxi)

#Mínimo valores
print("Mínimo valores")
mini = df.groupby(df["diagnosis"]).min()
print(mini)