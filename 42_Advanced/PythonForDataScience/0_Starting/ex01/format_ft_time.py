import datetime
import time

print(f"Seconds since January 1, 1970: {time.time():,.4f} or {time.time():.2e}\
 in scientific notation\n{datetime.datetime.now():%b %d %Y}")
