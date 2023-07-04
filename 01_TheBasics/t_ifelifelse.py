
import datetime

today = datetime.date.today().weekday()

week = ['Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday']

if today == 0:
  print("today is party, it's: ", week[today])
elif today == 6:
  print("today is party, it's: ", week[today])
else:
  print("work, work, work, it's: ", week[today])