import pytz
from datetime import *
tz_london = pytz.timezone("Europe/London")
datatime_london = datetime.now(tz_london)
time_london =   datatime_london.strftime("%d/%m/%y , %H:%M:%S")
print(f"time_london {time_london}")

tz_NY = pytz.timezone("America/New_York")
datatime_NY = datetime.now(tz_NY)
time_NY =   datatime_NY.strftime("%d/%m/%y , %H:%M:%S")
print(f"time_NY {time_NY}")

tz_paris = pytz.timezone("Europe/Paris")
datatime_paris = datetime.now(tz_paris)
time_paris =   datatime_paris.strftime("%d/%m/%y , %H:%M:%S")
print(f"time_paris {time_paris}")