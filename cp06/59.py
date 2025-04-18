import gensim
import matplotlib.pyplot as plt
import numpy as np
import pycountry
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans



model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

countrys = pycountry.countries
country_name = []
for country in countrys:
    country_name.append(country.name.replace(' ', '_'))

vec_list = []
country_name_fix = []

for name in country_name:
    try:
        vec = np.array(model.get_vector(name),"float64")
        vec_list.append(vec)
        country_name_fix.append(name)
    except:
        pass

vec_list = np.array(vec_list)
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(vec_list)
pred = KMeans(n_clusters = 5, random_state=42).fit_predict(vec_list)

plt.figure(figsize=(15, 13))
col_list = ["Blue", "Red", "Green", "Black"]
for X, name, km in zip(X_tsne, country_name_fix, pred):
    plt.plot(X[0], X[1], color = col_list[km-1], marker="o")
    plt.annotate(name, xy=(X[0], X[1]))
plt.title("T-SNE")
plt.savefig("59.png")
plt.show()