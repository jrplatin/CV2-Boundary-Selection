import numpy as np
import argparse
import cv2
import webcolors

#obtain command-cline arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
#set the image var
image = cv2.imread(args["image"])

#set RGB boundaries
boundaries = [
([17, 15, 100], [50, 56, 200]),
([86, 31, 4], [220, 88, 50]),
([25, 146, 190], [62, 174, 250]),
([0,61,0], [0,255,0]),
([64, 80,60],[70, 90, 84]),
([18,58,10], [36,148,124]),
([24, 121, 157], [91, 169, 205])
]

array = []
for i in range(0, len(boundaries) -1):
    first_tuple_lower_blue = boundaries[i][0][0] 
    first_tuple_lower_red = boundaries[i][0][2] 
    first_tuple_lower_green = boundaries[i][0][1] 

    first_tuple = (first_tuple_lower_red, first_tuple_lower_green, first_tuple_lower_blue)


    second_tuple_lower_blue = boundaries[i][1][0] 
    second_tuple_lower_red = boundaries[i][1][2] 
    second_tuple_lower_green = boundaries[i][1][1] 

    second_tuple = (second_tuple_lower_red, second_tuple_lower_green, second_tuple_lower_blue)

array = ["red", "blue", "green", "yellow", "dark green", "blue", "green again"]

i = 0
for (lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    
    #create the mask relating to each boundary
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    ratio_brown = cv2.countNonZero(mask)/(image.size/3)
    print(array[i] + 'pixel percentage:', np.round(ratio_brown*100, 2))
    i = i+1

    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)