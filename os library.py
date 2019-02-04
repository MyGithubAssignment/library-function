'''# os library
import os
print("my current working directory:",os.getcwd())
print("BISHA BHANDARI",os)

#print the current weekday,weekmonth and year in seperate statements:
import datetime as dt
dayofweek = dt.datetime.today().strftime("%A")
week_of_month=dt.datetime.today()
print(week_of_month)
print(dayofweek)

import calendar
for name in calendar.month_name:
    print(name)

import calendar
for day in calendar.day_name:
    print(day)

#use two functions from the math library:
#a
import math as m
x=int(input("enter the value of x:"))
print(m.sqrt(x))

#b
import math as m
x=int(input("enter the value of x:"))
print(m.cos(x))

#c
import math as m
z=int(input("enter the value of z:"))
print ("The e**z value is : ", end="")
print (m.exp(z))


#find the more library functions:
#a
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine wave form")

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()

#webbrowser library
import webbrowser
a=input("Search video")
print("Opening video")
webbrowser.open_new_tab('http://youtube.com/search?q=%s'%a)

#os library
import os
print(os.environ)
import os
print(os.uname())
'''
#c
from PIL import Image
import glob, os
size = 128, 128
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + ".thumbnail", "JPEG")






