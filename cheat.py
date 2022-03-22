import math
import cv2 as cv
import json
import time

from cv2 import sqrt

resized = cv.imread("1.jpg")

file = open("data.txt", "w")

def find_cont(img):

    out = 30
    poses = []

    for y in range(0, img.shape[0]-2, 2):

        for x in range(0, img.shape[1]-1, 2):
            s = False
            for c in range(0, 3):
                try:
                    if img[y][x][c] > img[y-1][x-1][c]-out and img[y][x][c] < img[y-1][x-1][c]+out:
                        if img[y][x][c] > img[y][x-1][c]-out and img[y][x][c] < img[y][x-1][c]+out:
                            if img[y][x][c] > img[y-1][x][c]-out and img[y][x][c] < img[y-1][x][c]+out:
                                if img[y][x][c] > img[y-1][x+1][c]-out and img[y][x][c] < img[y-1][x+1][c]+out:
                                    s = True
                except IndexError:
                    print("mo")
                    None
            if s:
                continue
            poses.append((x, y))
            
    
    return(poses)

fin = {}
l = find_cont(resized)
k1 = 0
k2 = 0
for t in range(1, 401, 20):
    fin[t] = []
    print(t)

    for t2 in range(141, len(l), 1):
        if t2 == t:
            continue
        print(t2)
        cv.circle(resized, (l[t][0], l[t][1]), 3, (0, 0, 0))
        cv.circle(resized, (l[t2][0], l[t2][1]), 3, (0, 0, 100))   
        cv.circle(resized, (l[t2-1][0], l[t2-1][1]), 1, (0, 0, 255))  
        cv.imshow("hi", resized)
        cv.waitKey(0)   
        print((l[t][0], l[t][1]))
        print((l[t2][0], l[t2][1]))
        print((l[t2-1][0], l[t2-1][1]))
        l01 = math.sqrt(((l[t][0]-l[t2][0])**2)+((l[t][1]-l[t2][1])**2))
        l02 = math.sqrt(((l[t][0]-l[t2-1][0])**2)+((l[t][1]-l[t2-1][1])**2))

        try:
            k1 = l01/l02
        except ZeroDivisionError:
            None
       
        #fin[t].append((l01-l1, l02-l2))

 
#with open("data_file.json", "w") as write_file:
#    json.dump(fin, write_file)

"""for i in range(0, len(all_y)):
    cv.circle(an_img, (all_x[i], all_y[i]), 1, (0, 0, 255))
cv.imshow("res", an_img)
cv.waitKey(0)"""