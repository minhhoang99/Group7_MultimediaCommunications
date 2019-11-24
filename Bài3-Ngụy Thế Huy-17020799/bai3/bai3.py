import cv2

path = "./image_test/alpha.png"

# read image from source with option grayscale => black whihte image
b_w = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# save balck white image
cv2.imwrite('./result/blackwhite.png',b_w)


# read image with option flag = -1 to keep all channel of image
img = cv2.imread(path,-1)

# split image => 4 channel 
b,g,r,a = cv2.split(img)

# save channel => image
cv2.imwrite('./result/BChannel.png',b)
cv2.imwrite('./result/GChannel.png',g)
cv2.imwrite('./result/RChannel.png',r)
cv2.imwrite('./result/AChannel.png',a)

# merge 4 channel => origin image
img=cv2.merge((b,g,r,a))
# save image after merge
cv2.imwrite('./result/MergedOutput.png',img)
