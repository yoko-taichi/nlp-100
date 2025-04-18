import numpy as np
import gensim
import pprint

model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

pprint.pprint(model.most_similar_cosmul(positive=["Spain", "Athens"], negative=["Madrid"], topn=10))
