# Import
import numpy as np
import cv2 
import mahotas
import os
import glob

# Path
# Definition = 'Train/crop_string_2'
Definition = 'Val/crop_string_val_2'

path0 = 'C:/Users/ffriz/Desktop/Data/'+Definition+'/_Original/'
path1 = 'C:/Users/ffriz/Desktop/Data/'+Definition+'/Blur'
path2 = 'C:/Users/ffriz/Desktop/Data/'+Definition+'/Bin'
path3 = 'C:/Users/ffriz/Desktop/Data/'+Definition+'/A_Bin'
path4 = 'C:/Users/ffriz/Desktop/Data/'+Definition+'/Otsu'
path5 = 'C:/Users/ffriz/Desktop/Data/'+Definition+'/Canny'
path6 = 'C:/Users/ffriz/Desktop/Data/'+Definition+'/Sobel'



# Read the files
#img_o1 = cv2.imread('a.jpg')

img_o = [cv2.imread(file) for file in glob.glob(path0+"*.jpg")]

# Vector size
ln=len(img_o)

# Matrices
img = suave = {}
result1 = result2 = result3 = result4 = result5 = result6 = {}

###############################################################################
# RGB to Gray
for i in range(0,ln):
    img[i] = cv2.cvtColor(img_o[i], cv2.COLOR_BGR2GRAY)
 
###############################################################################
# Apply blur 
for i in range(0,ln):
    suave[i] = cv2.GaussianBlur(img[i], (5, 5), 0)
    cv2.imwrite(os.path.join(path1,'GB_%02i.jpg' %i), suave[i]) # GaussianBlur

###############################################################################
# Binarization with threshold
for i in range(0,ln):
    (T, binI) = cv2.threshold(suave[i], 160, 255, cv2.THRESH_BINARY_INV)
    result1[i] = np.vstack([np.hstack([cv2.bitwise_and(img[i], img[i], 
        mask = binI)])])
    cv2.imwrite(os.path.join(path2,'BL_%02i.jpg' %i), result1[i]) # Binarizacao_limiar    
      
###############################################################################
# Adaptive threshold
for i in range(0,ln):
    bin2 = cv2.adaptiveThreshold(suave[i], 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)
    cv2.imwrite(os.path.join(path3,'BT_%02i.jpg' %i), result2[i]) # Binarizacao_Threshold
     
###############################################################################
# Threshold with Otsu and Riddler-Calvard
for i in range(0,ln):
    T = mahotas.thresholding.otsu(suave[i])
    temp = img[i].copy()
    temp[temp > T] = 255
    temp[temp < 255] = 0
    temp = cv2.bitwise_not(temp)
    T = mahotas.thresholding.rc(suave[i])
    temp2 = img[i].copy()
    temp2[temp2 > T] = 255
    temp2[temp2 < 255] = 0
    temp2 = cv2.bitwise_not(temp2)
    result3[i] = np.vstack([np.hstack([temp2])]) 
    cv2.imwrite(os.path.join(path4,'BO_%02i.jpg' %i), result3[i]) # Binarizacao (Thres.) Otsu e Rid.
     
###############################################################################
# Canny
for i in range(0,ln):
    canny1 = cv2.Canny(suave[i], 20, 100)
    result4[i] = np.vstack([canny1])
    cv2.imwrite(os.path.join(path5,'CN_%02i.jpg' %i), result4[i]) # Cany
   
###############################################################################
# Sobel
for i in range(0,ln):
    sobelX = cv2.Sobel(suave[i], cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(suave[i], cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    sobel = cv2.bitwise_or(sobelX, sobelY)
    result5[i] = np.vstack([sobel]) 
    cv2.imwrite(os.path.join(path6,'SB_%02i.jpg' %i), result5[i]) # Sobel