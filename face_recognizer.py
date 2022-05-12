from imutils import face_utils
import dlib
import cv2
import database


# the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

# start webcam
cap = cv2.VideoCapture(0)

# create database
db = database.Database()
db.create_db()

while True:

    if not cap.isOpened():
        print('Unable to load camera.')
        break

    else:
        _, image = cap.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        rects = detector(gray, 0)

        # loop over the face detections
        for (i, rect) in enumerate(rects):

            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            decode = shape.tolist()

            # insert database
            db.collections(decode)
            # update database
            num = db.read(decode)

            (x, y, w, h) = face_utils.rect_to_bb(rect)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, str(num), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("Output", image)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

cv2.destroyAllWindows()
cap.release()