import matplotlib.pyplot as plt

def iris_mean(dataset):
	df = dataset.groupby(5).mean().dropna()
	df.drop(0, axis=1, inplace=True)
	print(df)
	#x = [1, 2, 3, 4]
	color = ["red", "blue", "green"]
	x = ["sepal length", "sepal width", "petal length", "petal width"]
	fig, ax = plt.subplots(len(df.index), 1, figsize=(10,7), sharex=True)
	i = 0
	for name, data in df.iterrows():
		ax[i].bar(x, data, color=color[i])
		ax[i].set_title("Plant: " + name)
		ax[i].set_ylabel("Mean")
		i += 1
	ax[i-1].set_xlabel("Attribute")
	fig.subplots_adjust(hspace=1)
	plt.show()
