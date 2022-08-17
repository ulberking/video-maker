import cv2
import os
path = 'PRO-105-Reference-Code-Student-Activity-main/Images'
allImages = os.listdir(path)

images = []
for i in allImages:
    finalFileName = path + '/' + i
    images.append(finalFileName)
frame = cv2.imread(images[0])
height, width, channels = frame.shape
sizes = (width,height)
newVideo = cv2.VideoWriter('PRO-105-Reference-Code-Student-Activity-main/Sunset.mp4', cv2.VideoWriter_fourcc(*'DIVX'),10,sizes)
for i in  images:
    frame=cv2.imread(i)
    newVideo.write(frame)
newVideo.release()
cv2.destroyAllWindows()