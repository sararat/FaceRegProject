import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendentrealtime-3df78-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
     "524658": {
        "id": "524658",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "KKTECH",
        "name": "Sittisak Prempoon",
        "standing": "G",
        "starting_year": 2017,
        "total_attendance": 0,
        "year": 4
    }, 
    "524659": {
        "id": "524659",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "nontan",
        "name": "Jittima Jantarama",
        "standing": "G",
        "starting_year": 2017,
        "total_attendance": 0,
        "year": 4
    },
    "524657": {
        "id": "524657",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Sararat Wannajam",
        "standing": "G",
        "starting_year": 2017,
        "total_attendance": 0,
        "year": 4
    }, 
    "67319010001": {
        "id": "67319010001",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Kanin Kongsu",
        "standing": "1/1",
        "starting_year": 2017,
        "total_attendance": 0,
        "year": 4
    },
    "67319010004": {
        "id": "67319010004",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Jirawat Donbuntao",
        "standing": "1/1",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010005": {
        "id": "67319010005",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Chayaporn Harigun",
        "standing": "1/1",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010006": {
        "id": "67319010006",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Chanachai Sankod",
        "standing": "1/1",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010007": {
        "id": "67319010007",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Nutchapol Kaewteentan",
        "standing": "1/1",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010009": {
        "id": "67319010009",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Taksin Pimwan",
        "standing": "1/1",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010010": {
        "id": "67319010010",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Tuedsak Chokprakong",
        "standing": "1/1",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010011": {
        "id": "67319010011",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Narathon Jupamattung",
        "standing": "1/2",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010012": {
        "id": "67319010012",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Pratumwan Jaruensit",
        "standing": "1/1",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010013": {
        "id": "67319010013",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Patcharapol Promchat",
        "standing": "1/1",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010014": {
        "id": "67319010014",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Peerapol naknang",
        "standing": "1/2",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010018": {
        "id": "67319010018",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Wararak Singsawang",
        "standing": "1/2",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010018": {
        "id": "67319010018",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Wararak Singsawang",
        "standing": "1/2",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010019": {
        "id": "67319010019",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Watthigon Boonserm",
        "standing": "1/2",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010020": {
        "id": "67319010020",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Weeraporn Jansopa",
        "standing": "1/2",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010023": {
        "id": "67319010023",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Apiwat Pangnoi",
        "standing": "1/2",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010028": {
        "id": "67319010028",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Thapanawat Panvijit",
        "standing": "1/2",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010033": {
        "id": "67319010033",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Tanawat Kommueng",
        "standing": "1/2",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010038": {
        "id": "67319010038",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Rattapom Sakeaw",
        "standing": "1/2",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010039": {
        "id": "67319010039",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Waraporn Tonlow",
        "standing": "1/2",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
    "67319010044": {
        "id": "6731901004",
        "last_attendance_time": '2023-10-20 15:30:00',
        "major": "Information Technology",
        "name": "Sudpisat Wongfun",
        "standing": "1/1",
        "starting_year": 2020,
        "total_attendance": 0,
        "year": 1
    },
}

for key, value in data.items():
    ref.child(key).set(value)
