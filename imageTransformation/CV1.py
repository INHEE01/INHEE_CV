from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

im = Image.open('building.jpg')
im = np.asarray(im)
print(im.shape, im.dtype)

plt.figure() # figure 만들어두면 좋다.
plt.imshow(im)
plt.show()

# (400, 600, 3) 출력되는데 400 부분 -> Height / 600 -> Weight / 3 -> RGB / uint8 -> unsigned Int 8
# 중요!! float 를 imshow 해서 넣으려면 정규화해야한다!!
""" point processing : increase brightness """
im2 = im + 100.0
im2[im2>=255] = 255 # im2 값이 255를 넘어간다면 255로 고정한다. 왜냐? 255 넘어가면 pixel 최대값 overflow 로 이미지가 깨지게 됨.
plt.figure()
plt.imshow(im2/255.0) # 정규화
plt.show()

# Lower cotrast 는 직접 해보자! im/alpha -> alpha 값을 2 or 3 으로 해보자!
