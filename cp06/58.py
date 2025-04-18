from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import gensim
import numpy as np
import pycountry


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

fig = plt.figure(figsize=(20, 10))
Z = linkage(vec_list, 'ward')
dn = dendrogram(Z, labels = country_name_fix)
plt.show()

fig.savefig("58.png")
