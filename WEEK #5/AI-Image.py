from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('dog.jpg')
img_np = np.array(img) # 행렬로 변환된 이미지
plt.imshow(img_np) # 행렬 이미지를 다시 이미지로 변경해 디스플레이
plt.show() # 이미지 인터프린터에 출력

