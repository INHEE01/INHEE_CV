from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

im = Image.open('building.jpg')
im = np.asarray(im)
print(im.shape, im.dtype)

plt.figure() # figure 만들어두면 좋다.
plt.imshow(im)
# plt.show()

# (400, 600, 3) 출력되는데 400 부분 -> Height / 600 -> Weight / 3 -> RGB / uint8 -> unsigned Int 8
# 중요!! float 를 imshow 해서 넣으려면 정규화해야한다!!
""" point processing : increase brightness """
im2 = im + 100.0
im2[im2>=255] = 255 # im2 값이 255를 넘어간다면 255로 고정한다. 왜냐? 255 넘어가면 pixel 최대값 overflow 로 이미지가 깨지게 됨.
plt.figure()
plt.imshow(im2/255.0) # 정규화
# plt.show()

# Lower cotrast 는 직접 해보자! im/alpha -> alpha 값을 2 or 3 으로 해보자!
im3 = im/2
plt.figure()
plt.imshow(im3/255.0) # 정규화
# plt.show()

a = np.array([
              [1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]
            ])

# 위 배열에서 8 을 추출한다.
print(a[2][1])
# 5, 6, 8, 9, 11, 12 추출하기
print(a[1:4,1:3]) 
# 7, 8, 9, 10, 11, 12 추출하기
print(a[2:4,0:3])

# filtering using a box filter
k = 3 # kernel size
kernel = np.ones([k,k])/9.0 # 9.0 = k * k 값
Y, X = im.shape[0], im.shape[1]
p = k//2 # 스킵해야하는 픽셀의 수. 예제에서는 p=1임.
Y_out, X_out = Y - 2*p, X-2*p # Y-2, X-2
output = np.zeros([Y_out, X_out, im.shape[2]]) # shape 2 -> channel size

for y in range(p, Y-p):
    for x in range(p, X-p):
        yo, xo = y-p, x-p
        output[yo, xo, 0] = np.sum(im[y-p:y+p+1, x-p:x+p+1, 0]*kernel) # RGB / 0 -> R / 1 -> G / 2 -> B /
        output[yo, xo, 1] = np.sum(im[y-p:y+p+1, x-p:x+p+1, 1]*kernel)
        output[yo, xo, 2] = np.sum(im[y-p:y+p+1, x-p:x+p+1, 2]*kernel)

plt.figure()        
plt.imshow(output/255.0)
plt.show()

# 21