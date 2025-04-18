from scipy.stats import spearmanr
import gensim
import pandas as pd

def cos_sim(X):
    return model.similarity(X["Word 1"], X["Word 2"])

model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
df = pd.read_csv("wordsim353/combined.csv")
wordvec = df.apply(cos_sim, axis=1)
correlation, pvalue = spearmanr(wordvec, df["Human (mean)"])
print("スピアマン相関係数:", correlation)
print("p値:", pvalue)