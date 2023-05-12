import pandas as pd
import barplot

# chargement du dataset
iris_data = pd.read_csv("iris.csv", header=None)

print("\n### Affichage des 5 premieres lignes du dataset")
print(iris_data.head(10))

print("\n### affichage des variables ###")
print(iris_data.info())

print("\n### calculs stats du dataset##")
print(iris_data.describe())

print("\n### comptage des valeurs regroupées par nom ###")
print(iris_data.groupby(5).count())

print("### bar plot ###")
print(barplot.iris_mean(iris_data))
