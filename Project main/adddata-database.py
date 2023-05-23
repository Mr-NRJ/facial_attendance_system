import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceacckey.json")
firebase_admin.initialize_app(cred,{
    'your realtime database/"
})

ref = db.reference('Students')

data = {
    "CSU19A44":
        {
            "name": "Neeraj S Hari",
            "major": "Computer Science",
            "Starting_Year": 2019,
            "Total_attendance":10,
            "Year":4,
            "Last_attendance": "2023-05-22 15:16:33"
        },
    "CSU19A64":
        {
            "name": "Abhijith",
            "major": "Buisness",
            "Starting_Year": 2020,
            "Total_attendance": 5,
            "Year": 3,
            "Last_attendance": "2023-05-22 15:16:33"
        },
    "CSU19A66":
        {
            "name": "Gopas prem",
            "major": "Electronics",
            "Starting_Year": 2021,
            "Total_attendance": 8,
            "Year": 2,
            "Last_attendance": "2023-05-22 15:16:33"
        },
    "CSU19A17":
        {
            "name": "Ashique Ali P S",
            "major": "Electrical",
            "Starting_Year": 2018,
            "Total_attendance": 11,
            "Year": 4,
            "Last_attendance": "2023-05-22 15:16:33"
        },
}

for key,value in data.items():
    ref.child(key).set(value)
