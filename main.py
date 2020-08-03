'''
Created on 22 июл. 2019 г.

@author: ivan
'''

import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    pass

print("started")
im = input('input filename\n')
# A = img.imread("herb.bmp")
A = img.imread(im + ".bmp")
A = np.array(A)
#print(A)
# plt.imshow(A)
# plt.show()


A[A < 128] = 0
A[A >= 128] = 1
A = 1 - A
# print(A)
# print(1-A)
s = np.shape(A)
# print(s[0])
k = 0
su = np.sum(A)
# print(su)
x1 = np.zeros(su, 'int')
y1 = np.zeros(su, 'int')
# print(np.shape(x1))

for i in np.arange(s[0]):
    for j in np.arange(s[1]):
        if A[i, j] == 1:
            x1[k] = i
            y1[k] = j
            k += 1

# plt.plot(x1,y1)
# plt.show()


x = x1[0]
y = y1[0]

x2 = np.zeros(su, 'int')
y2 = np.zeros(su, 'int')
x2[0] = x
y2[0] = y

A[x, y] = 0

o = [1, 1, 0, -1, -1, -1, 0, 1, 1]
p = [0, -1, -1, -1, 0, 1, 1, 1, 0]

count = 1
while count < su:
    # print(np.max(A))
    if np.max(A) == 0:
        break
    i = 0
    while i < 8:
        if A[x + o[i], y + p[i]] == 0 and A[x + o[i + 1], y + p[i + 1]] == 1:
            x = x + o[i + 1]
            y = y + p[i + 1]
            # print(x)
            A[x, y] = 0
            x2[count] = x
            y2[count] = y
            count += 1
            if A[x + o[i+1], y + p[i+1]] == 1 and A[x + o[i], y + p[i]] == 0:
                i -= 3
                continue
            i = 0
            break
        i += 1
    if i == 0:
        continue
    rmin = 2000000
    for i in np.arange(s[0]):
        for j in np.arange(s[1]):
            if A[i, j] == 1:
                r = np.sqrt((x - i) ** 2 + (y - j) ** 2)
                if (r < rmin):
                    rmin = r
                    ii = i
                    jj = j
    x = ii
    y = jj
    # print(rmin)
    A[x, y] = 0
    x2[count] = x
    y2[count] = y
    count += 1

# ===============================================================================
# print(np.sum(A))
# print(x2)
# print(y2)
# ===============================================================================
print('done')
plt.plot(x2, y2)
out = np.vstack((x2, y2))
plt.show()
# plt.savefig('output.png')

np.savetxt(im + ".txt", out.T, fmt="%s", delimiter='    ')
