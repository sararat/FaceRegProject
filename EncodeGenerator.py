from uuid import uuid4
import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendentrealtime-3df78-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendentrealtime-3df78.appspot.com"
})


# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    # bucket = storage.bucket(app=appF)

    # blob = bucket.blob("Images/"+profilePic+".png")
    # urllib.request.urlretrieve(blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET'), ".\\img.png")
    bucket = storage.bucket()
    blob = bucket.blob(fileName)

    # new_token = uuid4()
    # metadata = {"firebaseStorageDownloadTokens": new_token}
    # blob.metadata = metadata
    blob.upload_from_filename(fileName)

    print(path)
    print(os.path.splitext(path)[0])
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
