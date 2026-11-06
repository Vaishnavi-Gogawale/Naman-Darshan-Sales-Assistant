from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client['temples_clone']

temples = [
  {"name": "Tirupati Balaji", "location": "Tirupati, Andhra Pradesh", "deity": "Lord Venkateswara", "darshan_timings": "3 AM - 9 PM", "entry_fee": "Free, Special Darshan Rs 300", "best_time": "Sep - Feb", "description": "Tirupati Balaji is one of the richest and most visited temples in India. Devotees come for Venkateswara darshan and tonsure."},
  {"name": "Shirdi Sai Baba", "location": "Shirdi, Maharashtra", "deity": "Sai Baba", "darshan_timings": "4 AM - 11 PM", "entry_fee": "Free", "best_time": "Oct - Mar", "description": "Shirdi is famous for Sai Baba temple. Thursday is the most crowded day. Aarti timings are Kakad Aarti 4:30 AM and Shej Aarti 10:30 PM."},
  {"name": "Vaishno Devi", "location": "Katra, Jammu", "deity": "Mata Vaishno Devi", "darshan_timings": "24 Hours", "entry_fee": "Free, Yatra Parchi required", "best_time": "Mar - Oct", "description": "Vaishno Devi yatra is a 13 km trek from Katra to Bhawan. Helicopter and pony services are also available."},
  {"name": "Kashi Vishwanath", "location": "Varanasi, Uttar Pradesh", "deity": "Lord Shiva", "darshan_timings": "3 AM - 11 PM", "entry_fee": "Free, Sugam Darshan Rs 300", "best_time": "Nov - Feb", "description": "Kashi Vishwanath is one of the 12 Jyotirlingas. Located on the banks of Ganga in Varanasi."},
  {"name": "Somnath", "location": "Somnath, Gujarat", "deity": "Lord Shiva", "darshan_timings": "6 AM - 9 PM", "entry_fee": "Free", "best_time": "Oct - Mar", "description": "Somnath is the first of the 12 Jyotirlingas. Famous for evening aarti and light and sound show."},
]

darshans = [
  {"temple": "Tirupati Balaji", "type": "Sarva Darshan", "price": 0, "duration": "4-6 hours"},
  {"temple": "Tirupati Balaji", "type": "Special Entry Darshan", "price": 300, "duration": "2-3 hours"},
  {"temple": "Shirdi Sai Baba", "type": "Free Darshan", "price": 0, "duration": "1-2 hours"},
]

db['temples'].delete_many({})
db['darshans'].delete_many({})
db['temples'].insert_many(temples)
db['darshans'].insert_many(darshans)
print("Ho gaya! temples:", db['temples'].count_documents({}))
print("darshans:", db['darshans'].count_documents({}))