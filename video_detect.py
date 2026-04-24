import cv2

face_cascade = cv2.CascadeClassifier("XML_FILES/haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier("XML_FILES/haarcascade_eye.xml")


smile_cascades = cv2.CascadeClassifier("XML_FILES/haarcascade_smile.xml")

video = cv2.VideoCapture(0)

while True:
    ret,  frame = video.read()
    
    frame = cv2.flip(frame,1)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    capture_faces = face_cascade.detectMultiScale(gray, 1.1,5)
    
    
    for (x,y,w,h) in capture_faces:
        
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,10)
        
        if len(eyes)>0:
            cv2.putText(frame,"Eye Detected", (x,y-30), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0,255,0),2)
            
        else:
            cv2.putText(frame,"Eye Not Detected",(x,y-30), cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
        
        smile = smile_cascades.detectMultiScale(roi_gray,1.1,10)
        
        if len(smile)>0:
            cv2.putText(frame,"Smile Detected",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
        else:
            cv2.putText(frame,"Smile Not Detected",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
        
    cv2.imshow("Video Detection",frame) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
    
video.release()
cv2.destroyAllWindows() 

            