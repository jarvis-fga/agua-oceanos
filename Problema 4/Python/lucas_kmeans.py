# Create by Lucas Andrade
# On 15 / 10 / 2017

import codecs
import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

features = [
    "mean_of_the_integrated_profile",
    "standard_deviation_of_the_integrated_profile",
    "excess_kurtosis_of_the_integrated_profile",
    "skewness_of_the_integrated_profile",
    "mean_of_the_DM_SNR_curve",
    "standard_deviation_of_the_DM_SNR_curve",
    "excess_kurtosis_of_the_DM_SNR_curve",
    "skewness_of_the_DM_SNR_curve",
    "class"
]

data = pandas.read_csv('../data/HTRU_2.csv', sep=",", names=features)
labels = data['class']

f1 = data.mean_of_the_integrated_profile
f2 = data.standard_deviation_of_the_integrated_profile
f3 = data.excess_kurtosis_of_the_integrated_profile
f4 = data.skewness_of_the_integrated_profile
f5 = data.mean_of_the_DM_SNR_curve
f6 = data.standard_deviation_of_the_DM_SNR_curve
f7 = data.excess_kurtosis_of_the_DM_SNR_curve
f8 = data.skewness_of_the_DM_SNR_curve

X = np.matrix(zip(f1, f2, f3, f4, f5, f6, f7, f8))

pca = PCA(n_components=2)
pca.fit(X)
new_pca = pca.transform(X)

# print("PCA:")
# print(new_pca)
print("PCA done")

kmeans = KMeans(n_clusters=4).fit(new_pca)
print("KMeans done")

xx = np.array([])
yy = np.array([])

for i in new_pca:
	xx = np.append(xx, i[0])
	yy = np.append(yy, i[1])

print("Start graph:")

# Plot the results
plt.figure("Problem 4")
h1,=plt.plot(xx[kmeans.labels_==0], yy[kmeans.labels_==0],'go')
h2,=plt.plot(xx[kmeans.labels_==1], yy[kmeans.labels_==1],'bo')
h3,=plt.plot(xx[kmeans.labels_==2], yy[kmeans.labels_==2],'mo')
h4,=plt.plot(xx[kmeans.labels_==3], yy[kmeans.labels_==3],'ro')

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.legend([h1, h2],['Group 1', 'Group 2'], loc='upper left')
plt.show()