# x = 5
# y = 10
# z =(x + y)
# print(z)

from datetime import datetime as dt
import sys

print("Pyhton Version: " + str(sys.version))

current_date = dt.now().strftime("%Y-%m-%d")

print("Today's Date:", current_date)