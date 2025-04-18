import pandas as pd

df = pd.read_csv('54.csv')
df_se = df[df['section'].str.contains('gram')]
df_sy = df[~df['section'].str.contains('gram')]
df_se_true = df_se[df_se['true_word']==df_se['predword']]
df_sy_true = df_sy[df_sy['true_word']==df_sy['predword']]


print(f'semantic analogy:{len(df_se_true)/len(df_se)}')
print(f'syntactic analogy:{len(df_sy_true)/len(df_sy)}')