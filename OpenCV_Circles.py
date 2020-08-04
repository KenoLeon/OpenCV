import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    # Change colorspace:
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.medianBlur(gray, 5)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()