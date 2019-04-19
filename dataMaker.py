import cv2
import numpy as np

vid = cv2.VideoCapture('videos/you4.mp4')
path = 'D:/naman/projects/talkingFingers/test/pos'
i = 0

while True:
    _, frame = vid.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    # for getting vertical & horizontal gradients
    #sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
    #sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)
    
    #edge detector
    edges = cv2.Canny(frame, 100, 120)

    cv2.imshow('original', frame)
    #cv2.imshow('laplacian', laplacian)
    #cv2.imshow('sobel x', sobelx)
    #cv2.imshow('sobel y', sobely)
    #cv2.imshow('edges', edges)

    # Saving helloOri
    frame = np.rot90(frame, 3)
    fileName = "test/pos/youOri/you4_%d.jpg" % i
    cv2.imwrite(fileName, frame)     # save frame as JPEG file      
    success,image = vid.read()

    # Saving helloLap
    #fileName = "test/pos/goodLap/good%d.jpg" % i
    #cv2.imwrite(fileName, laplacian)     # save frame as JPEG file      
    #success,image = vid.read()

    # Saving helloCanny
    #fileName = "test/pos/youCanny/you1_%d.jpg" % i
    #cv2.imwrite(fileName, edges)     # save frame as JPEG file      
    #success,image = vid.read()

    i = i + 1
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cv2.release()