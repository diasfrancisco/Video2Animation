import cv2

incoming_video = cv2.VideoCapture('')

if not incoming_video.isOpened():
    print('Cannot open camera')

while True:    
    ret, frame = incoming_video.read()
    if not ret:
        print('Error loading frame')
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

incoming_video.release()
cv2.destroyAllWindows()