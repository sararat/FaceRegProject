import os
import pickle
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime
from sklearn.metrics import accuracy_score, classification_report
import requests

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendentrealtime-3df78-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendentrealtime-3df78.appspot.com"
})

bucket = storage.bucket()

# def unlock_door():
#         response = requests.get("http://172.20.10.3/relay_off")
#         if response.status_code == 200:
#             print("Door unlocked")
#         else:
#           print("Failed to unlock door")


# def lock_solenoid_lock():
#       response = requests.get("http://172.20.10.3/relay_on")
#       if response.status_code == 200:
#           print("Solenoid locked")
#       else:
#           print("Failed to lock solenoid")



cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread("Resources/backgrounds.png", cv2.IMREAD_COLOR)

folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []
cap = cv2.VideoCapture(0)
register = False


while True:
    ok, img = cap.read()
    resized_frame = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(
                encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(
                encodeListKnown, encodeFace)
            print("matches", matches)
            print("faceDis", faceDis)

            matchIndex = np.argmin(faceDis)
            print("Match Index", matchIndex)

            if matches[matchIndex]:

                print("Known Face Detected")
                print(studentIds[matchIndex])
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = studentIds[matchIndex]
                
                predicted_label = "Known Person" if True in matches else "Unknown"
                actual_label = "Known Person"

                predicted_labels = ["Known Person", "Unknown"]
                actual_labels = ["Known Person",
                                 "Known Person"]
                
                accuracy = accuracy_score(actual_labels, predicted_labels)
                report = classification_report(actual_labels, predicted_labels)

                position = (230, 285)
                font = cv2.FONT_HERSHEY_COMPLEX
                font_scale = 1
                color = (0, 0, 255)
                thickness = 2
                print(f"Accuracy: {accuracy * 100:.2f}%")
                print("\nClassification Report:\n", report)
               
                cv2.putText(imgBackground, str(
                    accuracy*100), position, font, font_scale, color, thickness)
                #unlock_door()

                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.imshow("Face Attendance", imgBackground)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                    counter = 1
                    modeType = 1

        if counter != 0:

            if counter == 1:
                # Get the Data
                studentInfo = db.reference(f'Students/{id}').get()
                print(studentInfo)

                # Get the Image from the storage
                blob = bucket.get_blob(f'Images/{id}.png')
                # console.log("Document data:", blob.data());
                if blob is not None:
                    array = np.frombuffer(
                        blob.download_as_string(), dtype=np.uint8)
                    imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                else:
                    print(f"Blob 'Images/{id}.png' not found.")
                # Update data of attendance
                datetimeObject = datetime.strptime(studentInfo['last_attendance_time'],
                                                   "%Y-%m-%d %H:%M:%S")
                secondsElapsed = (
                    datetime.now() - datetimeObject).total_seconds()
                print(secondsElapsed)
                if secondsElapsed > 30:
                    ref = db.reference(f'Students/{id}')
                    studentInfo['total_attendance'] += 1
                    ref.child('total_attendance').set(
                        studentInfo['total_attendance'])
                    ref.child('last_attendance_time').set(
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modeType = 3
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 +
                                  414] = imgModeList[modeType]

            if modeType != 3:

                if 10 < counter < 20:
                    modeType = 2

                imgBackground[44:44 + 633, 808:808 +
                              414] = imgModeList[modeType]

                if counter <= 10:
                    cv2.putText(imgBackground, str(studentInfo['total_attendance']), (861, 125),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo['major']), (980, 550),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(id), (1006, 493),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo['standing']), (910, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(studentInfo['year']), (1025, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(studentInfo['starting_year']), (1125, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                    (w, h), _ = cv2.getTextSize(
                        studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset = (414 - w) // 2
                    cv2.putText(imgBackground, str(studentInfo['name']), (808 + offset, 445),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)
                    # imgStudent = np.array([])
                    # imgBackground = np.zeros((216, 216, 3))
                    imgBackground[175:175 + 216, 909:909 + 216] = imgStudent

                counter += 1

                if counter >= 20:
                    counter = 0
                    modeType = 0
                    studentInfo = []
                    imgStudent = []
                    imgBackground[44:44 + 633, 808:808 +
                                  414] = imgModeList[modeType]

    else:
        modeType = 0
        counter = 0

    cv2.imshow("Face Attendance", imgBackground)
    #lock_solenoid_lock()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #lock_solenoid_lock()
        break
