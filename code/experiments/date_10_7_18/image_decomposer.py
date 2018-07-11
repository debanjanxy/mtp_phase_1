import os
import cv2
import numpy as np
import scipy.misc
from keras.models import load_model

def is_well(img,model):
    flag = False
    img = np.reshape(img,(1,1,64,64))
    output = model.predict(img)
    if(output[0][1]==1.0):
        flag = True
    return flag

if __name__=="__main__":
    #read the image
    img_path = os.getcwd()+'/img/map_image.png'
    img1 = cv2.imread(img_path)
    img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    #define the window size
    window_r = 64
    window_c = 64

    #load the model
    model = load_model(os.getcwd()+'/model/model_v0_0.h5')
    print(model)

    #crop out each window from the map_image.png
    #save each window in output directory
    well_count = 0
    for r in range(0,img.shape[0],window_r):
        for c in range(0,img.shape[1],window_c):
            window = img[r:r+window_r,c:c+window_c]
            if is_well(window,model):
                cv2.rectangle(img1,(r,c),(r+window_r,c+window_c),(0,255,0),2)
                well_count += 1
    scipy.misc.imsave(os.getcwd()+'/output_img.png',img1)
    print("No. of wells: " + str(well_count))
