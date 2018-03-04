import cv2
import numpy as np

# mouse callback function
'''def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)'''

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.line(img,(0,0),(511,511),(255,0,0),5)
font = cv2.FONT_ITALIC
cv2.putText(img,'OpenCV',(10,400), font, 4,(255,255,255),4,cv2.LINE_AA)
pts  =  np.array ([[ 10 , 5 ], [ 20 , 30 ], [ 70 , 20 ], [ 50 , 10 ]],  np . int32 )
pts  =  pts.reshape (( - 1 , 1 , 2 ))
img  =  cv2.polylines( img , [ pts ], True , ( 0 , 255 , 255))
#cv2.namedWindow('pepaPy')
#cv2.setMouseCallback('image',draw_circle)

#while(1):
cv2.imshow('image',img)
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
