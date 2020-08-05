import cv2


# Callback function from trackbar
def onChange(x):
    # print(x)
    pass


cap = cv2.VideoCapture(0)
# Create Named window and trackbars:
cv2.namedWindow('openCV UI', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Brigthness', 'openCV UI', 0, 100, onChange)
cv2.createTrackbar('Contrast', 'openCV UI', 0, 100, onChange)


while(True):
    ret, frame = cap.read()

    # Get trackbar values
    brigthness = cv2.getTrackbarPos('Brigthness', 'openCV UI')
    contrast = (cv2.getTrackbarPos('Contrast', 'openCV UI')/100)+1
    # Change brigthness & contrast
    frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brigthness)

    cv2.imshow('openCV UI', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
