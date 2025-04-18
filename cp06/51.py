import numpy as np
import gensim

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

X = model['United_States']
Y = model['U.S.']

print(cos_sim(X, Y))
