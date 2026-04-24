import cv2 

face_cascade = cv2.CascadeClassifier("XML_FILES/haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier("XML_FILES/haarcascade_eye.xml")

smile_cascade = cv2.CascadeClassifier("XML_FILES/haarcascade_smile.xml")

image_path = ["Sample Pictures/face_1.jpg",
              "Sample Pictures/face_2.jpg",]
for path in image_path:

    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detect_faces = face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in detect_faces:
    
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
    
        roi_gray = gray[y:y+h, x:x+w]
        roi_image = image[y:y+h]
    
        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,10)
    
        if len(eyes)>0:
            cv2.putText(image,"Eyes Detected", (x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.6, (0,255,0), 2)
        else:
            cv2.putText(image,"Eyes Not Detected", (x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.6, (0,255,0), 2)
        
        smile = smile_cascade.detectMultiScale(roi_gray,1.1,10)
    
        if len(smile)>0:
            cv2.putText(image,"Smile Detected", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
        else: 
            cv2.putText(image,"Smile Not Detected", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0,255,0), 2)
    
    cv2.imshow(path, image)
    cv2.waitKey(0)
    
cv2.destroyAllWindows() 
    