import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

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
df["diagnosis"].value_counts().plot.pie(autopct='%1.1f%%', colors = ["lightgreen","pink"],labels=["Benignos","Malignos"],title="Tipos de Cáncer")
plt.show()
plt.savefig("tipos_cancer.png")

#Máximo valores
print("Máximo valores")
maxi = df.groupby(df["diagnosis"]).max()
print(maxi)

#Mínimo valores
print("Mínimo valores")
mini = df.groupby(df["diagnosis"]).min()
print(mini)
 
y = df["diagnosis"]
#selecciona todas las columnas menos la de diagnosis
x = df.drop(columns=["diagnosis"])
print(y)
print(x)
print('\n'*5)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

print(x_train,'\n'*3)
print(x_test,'\n'*3)
print(y_train,'\n'*3)
print(y_test,'\n'*3)