import os
import cv2

path = "Images"

Images = []

for i in os.listdir(path) :
    name, ext = os.path.splitext(i)
   
    if ext in ['.gif', '.png', '.jpg', '.jpeg', 'jfif',]:
     file_name = path+"/"+i

     print(file_name)
     Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])

height, width, channels =  frame.shape

size = (width, height)

print(size)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
   read = cv2.imread(Images[i])
   out.write(read)

print("Done")

out.release()

