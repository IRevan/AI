import pandas as pd
from konlpy.tag import Mecab

mecab = Mecab()
with open('data3/cleaned_output.txt', 'r', encoding='utf-8') as file:
    text = file.read()

x = mecab.pos(text)

ndf = pd.DataFrame(x)
ndf.columns = ['noun', 'pos']
ndf.to_csv('data3/pos.csv', index=False, encoding='utf-8')