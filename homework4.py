from datetime import datetime

def get_days_from_today(date):
    current_date = datetime.today()
    date_format = '%Y-%m-%d'
    date_obj= datetime.strptime(date, date_format)
    delta = current_date - date_obj
    return delta.days

try:
  print(get_days_from_today("2024-10-04"))
  print(get_days_from_today("2024-10-06"))
  print(get_days_from_today("2024-10-08"))
  print(get_days_from_today("jybgbh"))
except ValueError:
  print("Date format is not correct")


