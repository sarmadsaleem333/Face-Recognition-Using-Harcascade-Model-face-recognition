import cv2
import face_recognition


known_names=[]
known_embeding=[]

person1=face_recognition.load_image_file("person1.png")
person2=face_recognition.load_image_file("person2.png")


person1_encoding=face_recognition.face_encodings(person1)[0]
person2_encoding=face_recognition.face_encodings(person2)[0]


known_embeding.append(person1_encoding)
known_embeding.append(person2_encoding)

known_names.append("Ali Haider")
known_names.append("MSS")



# Web cam initializationAli Haide
video_capture=cv2.VideoCapture(0)
while True:
    # capture frame by frame 
    ret,frame=video_capture.read()

    # find all face locations in frame
    face_locations=face_recognition.face_locations(frame)  
    # encoding the frame and face locations
    face_encodings=face_recognition.face_encodings(frame,face_locations)

    for (top,right,bottom,left),face_encodings in zip (face_locations,face_encodings):
        matches=face_recognition.compare_faces(known_embeding,face_encodings)
        name="Unknown"

        print(matches,"ma")

        # if matches

        if True in matches:
            first_match_index=matches.index(True)
            name=known_names[first_match_index]
        

        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        cv2.putText(frame,name,(left,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

    cv2.imshow("Video",frame)

    if (cv2.waitKey(1)& 0xFF==ord("q")):
        break

video_capture.release()

cv2.destroyAllWindows()
        


