from datetime import datetime
from datetime import date

import pytz

tz = pytz.timezone('EST') 
current_time = datetime.now(tz)

print("Current time in Eastern United States is :", current_time.strftime("%H:%M"))

today = date.today()

print(today.strftime("%m/%d/%y"))