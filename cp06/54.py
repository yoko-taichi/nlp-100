import gensim
import pandas as pd
import tqdm

model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

def search_sim(word1, word2, word3):
    result = model.most_similar(positive=[word2, word3], negative=[word1], topn=1)[0]
    return result

with open('questions-words.txt', 'r') as f:
    words1 = []
    words2 = []
    words3 = []
    true_words = []
    pred_words = []
    sims = []
    sections = []
    lines = f.readlines()
    for line in tqdm.tqdm(lines):
        line.replace("\n", "")
        if line[0] == ":":
            line.replace(":", "")
            section = line
        else:
            word1, word2, word3, true_word = line.split(" ")
            sections.append(section)
            words1.append(word1)
            words2.append(word2)
            words3.append(word3)
            true_words.append(true_word.replace("\n", ""))
            result = search_sim(word1, word2, word3)
            pred_words.append(result[0])
            sims.append(result[1])

    df = pd.DataFrame({"word1":words1, "word2":words2, "word3":words3, "true_word":true_words,"section":sections, "predword":pred_words, "similary":sims})
    df.to_csv('54.csv')
    df
        
