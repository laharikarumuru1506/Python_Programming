import datetime
import webbrowser
import random
import time

list=["https://youtu.be/_P7X8tMplsw","https://youtu.be/fKl2JW_qrso","https://youtu.be/mO_dS3rXDIs"]
url=random.choice(list)
temp=int(input("enter the time to keep alarm: "))

source=datetime.datetime.now().strftime("%H:%M:%S").split(':')
#print(source)
hours=int(source[0])
minutes=int(source[1])
seconds=int(source[2])
#print(hours,minutes,seconds)
updated_time=hours*3600+minutes*60+seconds

count=temp
while count>0:
    mins, secs = divmod(count, 60)
    hrs=0
    if mins>60:
        hrs,mins=divmod(mins,60)
    print("{:02d}:{:02d}:{:02d}".format(hrs,mins, secs))
    updated_time+=1
    time.sleep(1)
    count-=1

else:
    webbrowser.open_new_tab(url)