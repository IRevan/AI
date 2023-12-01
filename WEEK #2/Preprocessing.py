from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import itertools


okt = Okt()
for i in range(1, 9):
    with open('./data/article{}.txt'.format(i), 'r', encoding='utf-8') as file:
        article = file.read()

    noun = okt.nouns(article)
    list_o = list(dict.fromkeys(noun))

    sr_o = pd.Series(list_o)
    sr_o.to_csv('./data/noun{}.csv'.format(i), index=False, encoding='utf-8')

noun1 = pd.read_csv('data/noun1.csv')
noun2 = pd.read_csv('data/noun2.csv')
noun3 = pd.read_csv('data/noun3.csv')
noun4 = pd.read_csv('data/noun4.csv')
noun5 = pd.read_csv('data/noun5.csv')
noun6 = pd.read_csv('data/noun6.csv')
noun7 = pd.read_csv('data/noun7.csv')
noun8 = pd.read_csv('data/noun8.csv')

noun = pd.concat([noun1, noun2, noun3, noun4, noun5, noun6, noun7, noun8], sort=False)
noun = noun.drop_duplicates()
noun.columns = ['noun']

Data = noun['noun'].values.tolist()

r = len(Data)
a = []
for i in range(r):
    a.append(okt.nouns(Data[i]))

c = []
for i in range(r):
    c.append(Counter(a[i]))

target_list = list(itertools.chain(*a))
tl2 = Counter(target_list)
tl = Counter({x: tl2[x] for x in tl2 if len(x) > 1})

wc = WordCloud(font_path='data/NanumBarunGothic.ttf', background_color='white', max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tl))

plt.figure(figsize=(30, 10))
plt.axis('off')
plt.imshow(cloud)
plt.show()
