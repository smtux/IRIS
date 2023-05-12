import pandas as pd

# URL du dataset IRIS
iris_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# chargement du dataset
iris_data = pd.read_csv(iris_url, header=None)

# Enregistrement du dataset
iris_data.to_csv("iris.csv")
 
