import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    # --------CASCADE---------

    # Convert to Greyscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Denoise (also try bluring, this is expensive )
    frame = cv2.fastNlMeansDenoising(frame, h=3, templateWindowSize=7, searchWindowSize=21)
    # Apply threshold
    frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    # Mirror image
    frame = cv2.flip(frame, 1)
    # --------***---------

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
