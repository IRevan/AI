import pandas as pd
from konlpy.tag import Mecab
import os
import re

path = "./data2/"
file_paths = os.listdir(path)
file_paths.sort()

# 출력 파일 경로
output_file_path = 'data3/merged_output.txt'

# 파일 합치기
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for file_path in file_paths:
        with open(path + file_path, 'r', encoding='utf-8') as input_file:
            content = input_file.read()
            output_file.write(content)
            # 다른 파일들 사이에 줄 바꿈 추가 (선택사항)
            output_file.write('\n\n')

def regex(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()
        cleaned_content = re.sub(r'<[^>]+>', '', content)
        cleaned_content = re.sub(r'氠瑢\s*', '', cleaned_content)
        cleaned_content = re.sub(r'\[[^\]]*\]', '', cleaned_content)
        cleaned_content = re.sub(r'\([^)]*\)', '', cleaned_content)
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_content)

# 사용 예시
input_path = 'data3/merged_output.txt'
output_path = 'data3/cleaned_output.txt'
regex(input_path, output_path)

mecab = Mecab()
with open('data3/cleaned_output.txt', 'r', encoding='utf-8') as file:
    text = file.read()

x = mecab.nouns(text)
sr = pd.DataFrame(x)
sr = sr.drop_duplicates()
sr.columns = ['noun']

sr.to_csv('noun.csv', index=False, encoding='utf-8')