import cv2 
harcascade="model/haarcascade_mcs_nose.xml"


print(harcascade)
video_capture=cv2.VideoCapture(0)


video_capture.set(3,640)
video_capture.set(4,480)

while True:

    ref,frame=video_capture.read()
    faceCascade=cv2.CascadeClassifier(harcascade)
    img_grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face=faceCascade.detectMultiScale(img_grey,1.1,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img_grey,(x,y),(x+w,y+h),(0,255,0),2)



    cv2.imshow("Video",img_grey)


    if cv2.waitKey(1) & 0xFF==ord("q"):
        break