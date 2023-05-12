import pandas as pd
import iris

# URL du dataset IRIS
iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# chargement du dataset
iris_data = pd.read_csv(iris_url, header=None)

print("\n### Affichage des 5 premieres lignes du dataset")
print(iris_data.head())

print("\n### affichage des variables ###")
print(iris_data.info())

print("\n### calculs stats du dataset##")
print(iris_data.describe())

print("\n### comptage des valeurs regroupées par nom ###")
print(iris_data.groupby(4).count())

iris.filtre(iris_data, "Iris-setosa")
