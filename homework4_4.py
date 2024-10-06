from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Pol Irk", "birthday": "2005.10.05"},
    {"name": "Paul Atreides", "birthday": "1980.10.06"},
    {"name": "Kate Smith", "birthday": "1992.10.07"},
    {"name": "Van Smith", "birthday": "1992.10.12"},
    {"name": "Iv Smith", "birthday": "1992.10.13"},
    {"name": "Boo Smith", "birthday": "1992.10.14"}
]

def get_upcoming_birthdays (users):
  current_day = datetime.today().date()
  last_greeting_day = current_day + timedelta(days = 7)
  upcoming_birthdays = []
  for user in users:
    user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    user_bd_greeting = user_birthday.replace(year = current_day.year)
    if user_bd_greeting < current_day: 
       user_bd_greeting = user_birthday.replace(year = current_day.year + 1)
    if last_greeting_day >= user_bd_greeting >= current_day:
      if user_bd_greeting.weekday() == 5 :
         user_bd_greeting = user_bd_greeting + timedelta(days=2)
      elif user_bd_greeting.weekday() == 6:
         user_bd_greeting = user_bd_greeting + timedelta(days=1)   
      upcoming_birthdays.append({"name": user["name"], "greeting_day": user_bd_greeting.strftime ("%Y.%m.%d")})
  return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
