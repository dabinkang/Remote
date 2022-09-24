import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while capture.isOpened():
    ret, frame = capture.read()
    cv2.imshow("test", frame)

    key = cv2.waitKey(1)&0xFF
    if key == ord('c'):
        cv2.imwrite('test.jpg', frame)
        break

capture.release()
cv2.destroyAllWindows()
