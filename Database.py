import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("attendance-using-face-recog-firebase-adminsdk-wcrzr-b3a8aa59c4.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://attendance-using-face-recog-default-rtdb.firebaseio.com/'
})


ref = db.reference('Students')
data = {
    "2215":
        {
            "name": "Sahil Sayyed",
            "major": "BScIT",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-04-23 07:48:12"
        },
    "2220":
        {
             "name": "Bill Gates",
            "major": "BAFF",
            "starting_year": 2022,
            "total_attendance": 9,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 07:54:34"
        },
    "2541":
        {
             "name": "Ms Dhoni",
            "major": "Bcom",
            "starting_year": 2022,
            "total_attendance": 4,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 07:56:38"
        },
    "2654":
        {
            "name": "Khan Anas",
            "major": "BMS",
            "starting_year": 2022,
            "total_attendance": 2,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 08:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)