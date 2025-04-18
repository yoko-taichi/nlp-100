from sklearn.cluster import KMeans
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
pred = KMeans(n_clusters = 5).fit_predict(vec_list)
dic = {}
for cat, name in zip(pred, country_name_fix):
    dic.setdefault(cat, []).append(name)

print(dic)