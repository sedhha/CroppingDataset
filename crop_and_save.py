import cv2
import numpy as np

from os.path import join
from os import listdir
saving_directory=r"G:\extra_stuff\python_files\saving_directory"
browsing_directory=r"G:\extra_stuff\python_files\browsing_directory"

images=listdir(browsing_directory)
image_arrays=[]
count=0
for image in images:
    im=cv2.imread(join(browsing_directory,image))
    exten="."+image.split(".")[-1]
    image_arrays.append(im)
    print(f"Image {image} has dimensions as {np.shape(im)[0]} X {np.shape(im)[1]}.")
    x,y,w,h=cv2.selectROI(im)
    cropped_image=im[y:y+h,x:x+w]
    cv2.imshow("Res",cropped_image)
    print(f"Image created status: {cv2.imwrite(join(saving_directory,str(count)+exten),cropped_image)}")
    count=count+1
    print("Process complete...")
cv2.destroyAllWindows()
    



